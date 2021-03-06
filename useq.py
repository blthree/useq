
import picoweb
from picoweb.utils import parse_qs
from aswitch import *
from machine import Pin
from mcp492x import MCP492x
import network
from time import sleep
# import pkg_resources
# import uerrno
# requires micropython-ulogging, micropython-uasyncio, micropython-pkg_resources

# ap_ssid = "useq"
# ap_password = "useq"
# ap_authmode = 3  # WPA2


# def start_ap(ap_ssid,ap_password,authmode):
#     wlan_ap = network.WLAN(network.AP_IF)
#     wlan_ap.active(True)
#     wlan_ap.config(essid=ap_ssid, password=ap_password, authmode=ap_authmode)

def wlan_connect(ssid='MYSSID', password='MYPASS'):
    # import network
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('connecting to:', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


wlan_connect('TangyNet', '7thheaven')
dac = MCP492x()
# app = picoweb.WebApp(__name__)
app = picoweb.WebApp(None) # workaround for sendfile see: https://github.com/pfalcon/picoweb/issues/15


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    html = open('index.html', 'r')
    for line in html.readlines():
        yield from resp.awrite(line)

@app.route("/main.js")
def js_main(req, resp):
    yield from app.sendfile(resp, 'main.js.gz', b"text/javascript", {"Content-Encoding": "gzip"})



def note_to_cv(notes):
    for x in notes:
        z = x-2
        y = z//3
        r = ((y+1)*84) + ((z-y+1)*83)
        yield r


@app.route("/update")
def update_seq(req, resp):
    global gates
    global dac_vals
    yield from picoweb.start_response(resp)
    qs = parse_qs(req.qs)
    notes = [int(x) for x in qs['data'].split(',')]
    gates = [int(x) for x in qs['gates'].split(',')]
    dac_vals = list(note_to_cv(notes))
    dac.set_notes(dac_vals)



led = Pin(5,Pin.OUT)
led.value(0)
def toggle_led(state, led, dac):
    if state == 0:
        led.value(0)
    else:
        led.value(1)
        dac.advance_note()
        
# register switch obj and functions
switch = Switch(Pin(22, Pin.IN, Pin.PULL_UP))
switch.close_func(toggle_led, (0,led,dac))
switch.open_func(toggle_led, (1,led,dac))

app.run(host='192.168.50.224')