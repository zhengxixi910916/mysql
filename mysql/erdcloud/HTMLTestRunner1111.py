"""
A TestRunner for use with the Python unit testing framework. It
generates a HTML report to show the result at a glance.

The simplest way to use this is to invoke its main method. E.g.

    import unittest
    import HTMLTestRunner

    ... define your tests ...

    if __name__ == '__main__':
        HTMLTestRunner.main()


For more customization options, instantiates a HTMLTestRunner object.
HTMLTestRunner is a counterpart to unittest's TextTestRunner. E.g.

    # output to a file
    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

    # run the test
    runner.run(my_test_suite)


------------------------------------------------------------------------
Copyright (c) 2004-2007, Wai Yip Tung
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name Wai Yip Tung nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# URL: http://tungwaiyip.info/software/HTMLTestRunner.html

__author__ = "Wai Yip Tung , bugmaster"
__version__ = "0.8.2"

import requests

from erdcloud import ApiStats
from erdcloud.CommonServerTest import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

"""
Change History

Version 0.8.2
* Show output inline instead of popup window (Viorel Lupu).

Version in 0.8.1
* Validated XHTML (Wolfgang Borgert).
* Added description of test classes and test cases.

Version in 0.8.0
* Define Template_mixin class for customization.
* Workaround a IE 6 bug that it does not treat <script> block as CDATA.

Version in 0.7.1
* Back port to Python 2.3 (Frank Horowitz).
* Fix missing scroll bars in detail log (Podi).
"""

# TODO: color stderr
# TODO: simplify javascript using ,ore than 1 class in the class attribute?

import datetime
import io
import sys
import unittest
from xml.sax import saxutils


# ------------------------------------------------------------------------
# The redirectors below are used to capture output during testing. Output
# sent to sys.stdout and sys.stderr are automatically captured. However
# in some cases sys.stdout is already cached before HTMLTestRunner is
# invoked (e.g. calling logging.basicConfig). In order to capture those
# output, use the redirectors for the cached stream.
#
# e.g.
#   >>> logging.basicConfig(stream=HTMLTestRunner.stdout_redirector)
#   >>>

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


# ----------------------------------------------------------------------
# Template

class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.

    Overall structure of an HTML report

    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: 'pass',
        1: 'fail',
        2: 'error',
    }

    DEFAULT_TITLE = 'Unit Test Report'
    DEFAULT_DESCRIPTION = ''
    DEFAULT_TESTER = 'PDM Tester'

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="utf-8"/>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <link href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.css" rel="stylesheet">
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.4.1/js/bootstrap.min.js"></script>
    <script src="http://apps.bdimg.com/libs/Chart.js/0.2.0/Chart.min.js"></script>
    <!-- <link href="https://cdn.bootcss.com/echarts/3.8.5/echarts.common.min.js" rel="stylesheet">   -->

    %(stylesheet)s
</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}

function toggle(id){
	var tb = document.getElementById(id);
	if(tb.style.display=='none') 
		tb.style.display='block';
	else 
		tb.style.display='none';
}

function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

%(heading)s
%(report)s
%(chart_script)s
</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending)

    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         {  }

/* -- heading ---------------------------------------------------------------------- */
h1 {
	font-size: 16pt;
	color: gray;
}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
	margin-left: 10px;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
    margin-left: 10px;
}
#result_table {
}
#header_row {
    font-weight: bold;
    color: #606060;
    background-color: #f5f5f5;
    border-top-width: 10px;
    border-color: #d6e9c6;
	font-size: 12px;
}
#result_table td {
    border: 1px solid #f5f5f5;
    padding: 2px;

}
#total_row  { font-weight: bold; }
.passClass  { background-color: #d6e9c6; }
.failClass  { background-color: #faebcc; }
.errorClass { background-color: #ebccd1; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

/* -- chars ---------------------------------------------------------------------- */
.testChars {margin-left: 150px;}

.btn-info1 {
    color: #fff;
    background-color: #d6e9c6;
    border-color: #d6e9c6;
}

.btn-info2 {
    color: #fff;
    background-color: #faebcc;
    border-color: #faebcc;
}

.btn-info3 {
    color: #fff;
    background-color: #ebccd1;
    border-color: #ebccd1;
}

</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """<div class='heading'>
<h1>%(title)s</h1>
%(parameters)s
<p class='description'>%(description)s</p>
</div>

<div style="float:left; margin-left: 10px;">
	<p> Test Case Pie charts </p>
	<a class="btn btn-xs btn-info1">-Pass-</a><br>
	<a class="btn btn-xs btn-info2">-Faild-</a><br>
	<a class="btn btn-xs btn-info3">-Error-</a><br>
</div>

<div class="testChars">
	<canvas id="myChart" width="250" height="250"></canvas>
</div>

"""  # variables: (title, parameters, description)

    # ------------------------------------------------------------------------
    # Pie chart
    #

    ECHARTS_SCRIPT = """
    <script type="text/javascript">
var data = [
	{
		value: %(error)s,
		color: "#ebccd1",
		label: "Error",
		labelColor: 'white',
		labelFontSize: '16'
	},
	{
		value : %(fail)s,
		color : "#faebcc",
		label: "Fail",
		labelColor: 'white',
		labelFontSize: '16'
	},
	{
		value : %(Pass)s,
		color : "#d6e9c6",
		label : "Pass",
		labelColor: 'white',
		labelFontSize: '16'
	}			
]

var newopts = {
     animationSteps: 100,
 		animationEasing: 'easeInOutQuart',
}

//Get the context of the canvas element we want to select
var ctx = document.getElementById("myChart").getContext("2d");

var myNewChart = new Chart(ctx).Pie(data,newopts);

</script>
	"""

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s:</strong> %(value)s</p>
"""  # variables: (name, value)

    # ------------------------------------------------------------------------
    # Report
    #

    REPORT_TMPL = """
<p id='show_detail_line' style="margin-left: 10px;">Show
<a href='javascript:showCase(0)' class="btn btn-xs btn-primary">Summary</a>
<a href='javascript:showCase(1)' class="btn btn-xs btn-danger">Failed</a>
<a href='javascript:showCase(2)' class="btn btn-xs btn-info">All</a>
<a href='javascript:showCase(3)' class="btn btn-xs btn-info" style="margin-left: 12px;"><span>测试通过率：%(pass_coverage)s</span></a>
</p>

%(service_report)s

<h4 style="display: inline-block; margin-left: 10px"> 测试接口报表:</h4>
<table id='result_table' class="table table-condensed table-striped">
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row' class="panel-title">
    <td>Test Group/Test case</td>
    <td>Count</td>
    <td>Pass</td>
    <td>Fail</td>
    <td>Error</td>
    <td>View</td>
</tr>
%(test_list)s
<tr id='total_row'>
    <td>Total</td>
    <td>%(count)s</td>
    <td class="text text-success">%(Pass)s</td>
    <td class="text text-danger">%(fail)s</td>
    <td class="text text-warning">%(error)s</td>
    <td>&nbsp;</td>
</tr>
</table>
"""  # variables: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">Detail</a></td>
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
        %(status)s</a>

    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        %(script)s
        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>%(status)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #
    # ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""
    ENDING_TMPL = r"""
    <div id='ending' style="margin-left: 10px; margin-right: 10px;">&nbsp;
    <div>
        <table class='table table-condensed table-striped'>
            <tr>
                <th>服务名</th>
                <th>版本</th>
                <th>已测试接口</th>
                <th>未测试接口</th>
                <th>测试覆盖率</th>
            </tr>
            %(body)s
        </table>
    </div>
    </div>
    """


# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult


class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.
    isAllinone = True

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        self.passrate = float(0)
        self.status = 0
        # self.outputBuffer=io.StringIO()
        # self.test_start_time = round(time.time(),2)

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.' + str(self.success_count))

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        try:
            driver = getattr(test, "driver")
            test.img = driver.get_screenshot_as_base64()
        except AttributeError:
            test.img = ""
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')


class HTMLTestRunner(Template_mixin):

    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None, package_json_list=None):
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

        # 各服务 package.json 列表
        self.package_json_list = package_json_list

    def run(self, test):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity)
        test(result)
        self.stopTime = datetime.datetime.now()
        self.generateReport(test, result)
        # print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []
        if result.success_count: status.append('Pass %s' % result.success_count)
        if result.failure_count: status.append('Failure %s' % result.failure_count)
        if result.error_count:   status.append('Error %s' % result.error_count)
        if status:
            status = ' '.join(status)
        else:
            status = 'none'
        return [
            ('Start Time', startTime),
            ('Duration', duration),
            ('Status', status),
        ]

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'HTMLTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        # ending = self._generate_service_report()
        chart = self._generate_chart(result)
        output = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            # ending=ending,
            chart_script=chart,
        )
        self.stream.write(output.encode('utf8'))

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                name=saxutils.escape(name),
                value=saxutils.escape(value),
            )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
        )
        return heading

    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                else:
                    ne += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc=desc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid + 1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        if (result.success_count + result.failure_count + result.error_count) == 0:
            pass_coverage = 0
        else:
            pass_coverage = HTMLTestRunner.compute_coverage(result.success_count, (
                    result.success_count + result.failure_count + result.error_count))
        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
            pass_coverage=str(pass_coverage),
            service_report=str(self._generate_service_report())
        )
        return report

    def _generate_chart(self, result):
        chart = self.ECHARTS_SCRIPT % dict(
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
        )
        return chart

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            ue = e
        else:
            ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )

        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'none'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_service_report(self):
        """
        生成测试报告表格数据
        :return:各个服务的服务名;已测试接口;未测试接口;接口复覆盖率
        """
        '''获取已测试的接口,用服务区分'''
        # 获取已测试接口集
        stats = ApiStats.stats()
        # 加载前缀字典
        service_name_path_dict = HTMLTestRunner.load_service_name_path()
        # 获取服务列表
        service_list = self.package_json_list
        # 定义表格id
        tid1 = 1
        tid2 = 2
        # 定义body
        body = ''
        service_map = {}
        service_name_map = {}
        tested_map = {}
        for service in service_list:
            service["tested_api_count"] = 0
            service_map[service["app_name"]] = service
            if _TestResult.isAllinone and (service["allinone"]) is not None:
                service_name = service["allinone"]
            else:
                service_name = service["service_name"]
            service_name_map[service_name] = service
        path_service_name_map = {}
        for service_name, path in service_name_path_dict.items():
            if (path is not None):
                for _path in path['path']:
                    path_service_name_map[_path] = service_name
            # path_service_name_map[]
        # for service in service_list:

        # 已测试接口body
        tested_api = ''
        # 已测试接口列表(url-(method))
        # app_name = service["app_name"]
        # if _TestResult.isAllinone and (service["allinone"]) is not None:
        #     service_name = service["allinone"]
        # else:
        #     service_name = service["service_name"]
        # 已测试接口数
        # service_apis = service_name_path_dict[service_name].get("path")
        # service_alais = service_name_path_dict[service_name].get("alais")

        api_list = []
        # body += '<tr>'
        # body += '<td>' + service_name + '</td>'
        # body += '<td>' + service['version'] + '</td>'
        # body += '''<td><button type="button">'''
        for ele in stats.get("apis"):
            # 获取api路径中服务标识
            api_type = ele.get("api").split("/")[1]
            service = service_name_map[path_service_name_map[api_type]]
            if _TestResult.isAllinone and (service["allinone"]) is not None:
                service_name = service["allinone"]
            else:
                service_name = service["service_name"]
            service_apis = service_name_path_dict[service_name].get("path")
            app_name = service["app_name"]
            if api_type in service_apis:
                service = service_map[app_name]
                if tested_map.get(service_name) is not None:
                    tested_api_count = int(tested_map[service_name])
                else:
                    tested_api_count = 0
                # if api_type in service_apis:
                # if api_type in service_name_path_dict.get(service["service_name"], ""):
                tested_api_count += 1
                api_list.append(ele.get("api") + '-' + ele.get("method"))
                # tested_api += '<tr><td style="height:25px;">' + ele.get("method") + '：' + ele.get(
                #     "api") + '</td></tr>'
                tested_map[service_name] = tested_api_count
            else:
                print(ele["api"])
        for app_name, tested_api_count in tested_map.items():
            service = service_name_map[app_name]
            service_alais = service_name_path_dict[app_name].get("alais")
            body += '<tr>'
            body += '<td>' + app_name + '</td>'
            body += '<td>' + service['version'] + '</td>'
            body += '''<td><button type="button">'''
            body += str(tested_api_count)
            body += '</button>'
            # body += '<table border="1" id="table' + str(tid1) + '" style="display:none" frame=void>'
            # body += tested_api
            # body += '</table>'
            body += '</td>'

            body += '''<td><button type="button" onClick="toggle('table''' + str(tid2) + '''')">'''
            # 获取服务下所有的接口
            apis = Api({
                "api-docs": '/' + service_alais + '/v2/api-docs'
            })
            # 返回该服务的所有接口数和接口列表
            all_api, all_api_list, ignore_api_count = HTMLTestRunner.get_all_apis_docs(apis, 'api-docs',
                                                                                       service["ignore_apis"])
            # 未测试接口body
            not_tested_api = HTMLTestRunner.check_not_test_api(api_list, all_api_list, service["ignore_apis"])
            # 接口覆盖率
            api_coverage = HTMLTestRunner.compute_coverage(tested_api_count, all_api)
            body += str(all_api - tested_api_count)
            body += '</button>'
            body += '<table border="1" id="table' + str(tid2) + '" style="display:none" frame=void>'
            body += not_tested_api
            body += '</table></td>'

            # 拼接覆盖率
            body += '<td>'
            body += api_coverage
            body += '</td></tr>'

            tid1 += 2
            tid2 += 2
            service_map[service_name] = tested_api_count

        return self.ENDING_TMPL % {
            "body": body
        }

    @staticmethod
    def load_service_name_path():
        """
        加载最新的prefix前缀
        :return: 前缀字典
        """
        # 发送请求，获取数据
        host = CommonServer().get_host()
        resp = requests.get(url=host + "/route/prefix")
        data = resp.json().get("res").get("data")

        if data:
            prefix_dict = {}
            for item in data:
                key = item.get("serviceName")
                if ("erdcloud-system-app" == key):
                    _TestResult.isAllinone = False
                path = item.get("path")
                if key != "" and path != "" and path is not None and len(path) > 0:
                    # prefix_dict[key] = value
                    prefix_dict[key] = item
            return prefix_dict
        else:
            return {}

    @staticmethod
    def compute_coverage(tested_api_count, test_all_api):
        """
        计算覆盖率，保留两位小数
        :param tested_api_count: 已测试接口数
        :param test_all_api: 总接口数

        :return: 覆盖率%
        """
        return str(round((tested_api_count / test_all_api * 100), 2)) + '%'

    @staticmethod
    def check_not_test_api(api_list, all_api_list, ignore_apis):
        """
        检查未测试接口
        :param api_list: 已测试接口 (url-(method))
        :param all_api_list: 所有接口 (url-(method))
        :return: 未测试接口 (url-(method))
        """
        not_test_api = ''
        all_api_format_list = []
        ignore_api_format_list = []
        for item in all_api_list:
            api = HTMLTestRunner.replace_char(item)
            all_api_format_list.append(api)
        for item in ignore_apis:
            api = HTMLTestRunner.replace_char(item)
            ignore_api_format_list.append(api)

        for format_api in all_api_format_list:
            if format_api not in api_list and format_api not in ignore_api_format_list:
                url = format_api.split("-")[0]
                method = format_api.split("-")[1]
                not_test_api += '<tr><td  style="height:25px;">' + method + '：' + url + '</td></tr>'

        return not_test_api

    @staticmethod
    def replace_char(api):
        """
        替换{}为%s
        :param:api
        :return:替换后的数据
        """
        count = api.count('{')
        i = 1
        while i <= count:
            start = api.find('{')
            end = api.find('}')
            api = api.replace(api[start:end + 1], '%s')
            i += 1
        return api

    @staticmethod
    def get_all_apis_docs(apis, key, ignore_apis=[]):
        """
        检查未测试接口
        :param apis: 接口对象
        :param key: 接口key
        :param ignore_apis: 忽略的api
        :return: 接口数,接口列表
        """
        all_count = 0
        ignore_api_count = 0
        all_api_list = []
        resp = RequestService.call_get(apis.get(key))
        paths = resp["paths"]
        total = 0
        # 该服务下所有接口
        for i, values in paths.items():
            for j in values:
                total += 1
        # 忽略的接口数
        ignore_apis_count = len(ignore_apis)
        # 要测试的接口数量
        all_api = total - ignore_apis_count
        # all_cnt = 0
        for k, value in paths.items():
            # all_cnt += 1
            method = list(value.keys())[0].upper()  # 获取字典的key返回list,获取第一个值(只有一个值)，全部大写
            # if HTMLTestRunner.containsIgnoreApi(k, ignore_apis):
            #     print(k + '-' + method)
            #     # ignore_api_count += 1
            #     continue
            # all_count += 1
            all_api_list.append(k + '-' + method)
        return all_api, all_api_list, ignore_apis_count
        # print(all_cnt)
        # return all_count, all_api_list, ignore_api_count

    @staticmethod
    def containsIgnoreApi(api, ignore_apis):
        for one in ignore_apis:
            if str(api).find(one) == 0:
                return True
        return False


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
