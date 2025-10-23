from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from threading import Thread
from Core.Networking.Server import Server

class ServerUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Server ist gestoppt")
        self.add_widget(self.label)
        self.button = Button(text="Server starten")
        self.button.bind(on_press=self.toggle_server)
        self.add_widget(self.button)
        self.server_thread = None
        self.running = False

    def toggle_server(self, instance):
        if not self.running:
            self.running = True
            self.button.text = "Server stoppen"
            self.label.text = "Server läuft auf Port 9339"
            self.server_thread = Thread(target=self.run_server)
            self.server_thread.start()
        else:
            self.running = False
            self.label.text = "Server gestoppt"
            self.button.text = "Server starten"
            # Hier müsstest du den Server sauber beenden (z. B. mit einem Stop-Flag in deiner Server-Klasse)

    def run_server(self):
        try:
            Server("0.0.0.0", 9339).start()
        except Exception as e:
            self.label.text = f"Fehler: {e}"

class MyApp(App):
    def build(self):
        return ServerUI()

if __name__ == '__main__':
    MyApp().run()