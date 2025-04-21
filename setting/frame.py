import wx
from wx import Button
from web import server
from automation import automator

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

    panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
    frame_sizer = wx.BoxSizer(wx.VERTICAL)

    left = set_left(panel)
    right = set_right(panel)

    panel_sizer.Add(left, 0)
    panel_sizer.Add(right, 0)
    panel.SetSizer(panel_sizer)

    frame_sizer.Add(panel, 1, wx.EXPAND)
    frame.SetSizerAndFit(frame_sizer)

def set_left(panel):
    left_panel = wx.Panel(panel, wx.ID_ANY)
    left_sizer = wx.BoxSizer(wx.VERTICAL)

    # 논리적 에러 뜨면 wx.Size 삭제
    execute_button: Button = wx.Button(left_panel, wx.ID_ANY, "서버 시작", size=wx.Size(330, 30))
    execute_button.Bind(wx.EVT_BUTTON, lambda event: server.start_server())
    execute_button.Enable(True)

    left_sizer.Add(execute_button, 0, wx.ALL, 10)

    left_panel.SetSizer(left_sizer)

    return left_panel

def set_right(panel):
    right_panel = wx.Panel(panel, wx.ID_ANY)
    right_sizer = wx.BoxSizer(wx.VERTICAL)

    # 논리적 에러 뜨면 wx.Size 삭제
    execute_button: Button = wx.Button(right_panel, wx.ID_ANY, "작업 수행", size=wx.Size(330, 30))
    execute_button.Bind(wx.EVT_BUTTON, lambda event: automator.start_task())
    execute_button.Enable(True)

    right_sizer.Add(execute_button, 0, wx.ALL, 10)

    right_panel.SetSizer(right_sizer)

    return right_panel

"""
실행 로직
"""


