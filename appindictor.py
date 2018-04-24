import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Mycroft")

        self.set_default_size(400,600)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(False)
        hb.props.title = "Mycroft Visual Interface"
        self.set_titlebar(hb)

        settings = Gtk.Button()
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        settings.add(image)
        hb.pack_end(settings)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box)


        self.outputbox = Gtk.ScrolledWindow()
        self.outputtext = Gtk.TextView()
        self.outputtext.set_editable(False)
        self.outputtext.set_cursor_visible(False)
        self.textbuffer = self.outputtext.get_buffer()
        self.outputbox.add(self.outputtext)
        box.pack_start(self.outputbox, True, True, 0)

        self.inputbox = Gtk.Box(spacing=3)
        box.pack_start(self.inputbox, True, True, 0)

        self.inputtext = Gtk.Entry()
        self.inputtext.set_activates_default(True)
        self.inputbox.pack_start(self.inputtext, True, True, 0)

        returnbutton = Gtk.Button.new_with_label('send')
        returnbutton.set_can_default(True)
        returnbutton.connect("clicked", self.send)
        self.inputbox.pack_start(returnbutton, True, True, 0)

        self.set_default(returnbutton)


    def send(self, widget):
        message = self.inputtext.get_text()
        print(message)
        self.inputtext.set_text("")


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()