class MCP492x:
    def __init__(self):
        from machine import SPI, Pin
        self.hspi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
        self.cs = Pin(33, Pin.OUT)
        self.ldac = Pin(32, Pin.OUT)
        self.base_val = 0b0111000000000000
        self.cs.value(1)
        self.ldac.value(1)
        self.note_index = 0
        self.notes = [[0 for x in range(8)] for y in range(2)] # 2x8 matrix
        

    def write(self, dac, val):
        dac_select_bit = 0b1000000000000000 if dac else 0b0
        buf = (self.base_val + val + dac_select_bit).to_bytes(2,1)
        self.cs.value(0)
        self.hspi.write(buf)
        self.cs.value(1)
        self.ldac.value(0)
        self.ldac.value(1)

    def set_notes(self, new_notes):
        self.notes = new_notes
    
    def advance_note(self):
        if self.note_index < 7:
            self.note_index +=1
        else:
            self.note_index = 0
        self.write(0,self.notes[self.note_index])
        self.write(1,self.notes[self.note_index])
     
