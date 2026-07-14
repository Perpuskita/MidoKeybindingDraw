class MidiException():
    def __init__(self):
        self.name = 'MIDI EXCEPTION'
    
    # gunakan http status code jika diperlukan
    def response(self, request_code):
        match request_code :
            case 400:
                return self.bad_request()

            case 404:
                return self.device_unconnected()
            
            case 500:
                return self.app_error()
            
            case _:
                return self.app_error()
    
    def device_unconnected(self):
        return f"{self.name} : device unconnected"
    
    def bad_request(self):
        return f"{self.name} : request not valid"
    
    def app_error(self):
        return f"{self.name} : app error "