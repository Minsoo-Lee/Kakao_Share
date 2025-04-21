import wx, time
from wx import Button
from web import server
from automation import automator
import wx.richtext as rt
from window import log
from automation import crawling

def run_wx():
    app = wx.App(False)
    frame = wx.Frame(None, wx.ID_ANY, "Kakao Share")
    set_frame(frame)
    frame.Show()
    app.MainLoop()
"""
frame Setting
일단 서버 시작, 프로그램 실행 두 가지 버튼으로 설정
"""
def set_frame(frame):
    panel = wx.Panel(frame, wx.ID_ANY)
    # panel.SetBackgroundColour(wx.Colour(160, 30, 240))

    button_sizer = wx.BoxSizer(wx.HORIZONTAL)
    frame_sizer = wx.BoxSizer(wx.VERTICAL)
    log_sizer = wx.BoxSizer(wx.VERTICAL)

    crawling_panel = set_crawling(panel)
    server_panel = set_server(panel)
    task_panel = set_task(panel)


    log_panel = set_log(panel)

    button_sizer.Add(crawling_panel, 0)
    button_sizer.Add(server_panel, 0)
    button_sizer.Add(task_panel, 0)

    log_sizer.Add(log_panel, 1, wx.EXPAND)

    panel_sizer = wx.BoxSizer(wx.VERTICAL)


    panel_sizer.Add(button_sizer, 0, wx.EXPAND, 5)
    panel_sizer.Add(log_sizer, 0, wx.EXPAND, 5)
    panel.SetSizer(panel_sizer)

    frame_sizer.Add(panel, 1, wx.EXPAND)
    frame.SetSizerAndFit(frame_sizer)

def set_crawling(panel):
    crawl_panel = wx.Panel(panel, wx.ID_ANY)
    crawl_sizer = wx.BoxSizer(wx.VERTICAL)

    # 논리적 에러 뜨면 wx.Size 삭제
    crawling_button: Button = wx.Button(crawl_panel, wx.ID_ANY, "크롤링", size=wx.Size(200, 30))
    crawling_button.Bind(wx.EVT_BUTTON, lambda event: crawling.start_crawling())
    crawling_button.Enable(True)

    crawl_sizer.Add(crawling_button, 0, wx.ALL, 5)

    crawl_panel.SetSizer(crawl_sizer)

    return crawl_panel

def set_server(panel):
    server_panel = wx.Panel(panel, wx.ID_ANY)
    server_sizer = wx.BoxSizer(wx.VERTICAL)

    # 논리적 에러 뜨면 wx.Size 삭제
    execute_button: Button = wx.Button(server_panel, wx.ID_ANY, "서버 시작", size=wx.Size(200, 30))
    execute_button.Bind(wx.EVT_BUTTON, lambda event: server.start_server())
    execute_button.Enable(True)

    server_sizer.Add(execute_button, 0, wx.ALL, 5)

    server_panel.SetSizer(server_sizer)

    return server_panel

def set_task(panel):
    task_panel = wx.Panel(panel, wx.ID_ANY)
    task_sizer = wx.BoxSizer(wx.VERTICAL)

    # 논리적 에러 뜨면 wx.Size 삭제
    task_button: Button = wx.Button(task_panel, wx.ID_ANY, "작업 수행", size=wx.Size(200, 30))
    task_button.Bind(wx.EVT_BUTTON, lambda event: automator.start_task())
    task_button.Enable(True)

    task_sizer.Add(task_button, 0, wx.ALL, 5)

    task_panel.SetSizer(task_sizer)

    return task_panel


def set_log(panel):
    log_panel = wx.Panel(panel, wx.ID_ANY)
    log_sizer = wx.BoxSizer(wx.VERTICAL)

    log_text_widget = rt.RichTextCtrl(log_panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(400, 500))
    log.set_log_widget(log_text_widget)  # 여기서 위젯 연결

    log_sizer.Add(log_text_widget, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
    log_panel.SetSizer(log_sizer)

    return log_panel
