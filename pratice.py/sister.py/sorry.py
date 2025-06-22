# Sister Apology Kivy App (Final Fixed Version with Animation and Music)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from datetime import datetime
import random
import os
import shutil
import webbrowser
from kivy.clock import Clock
import pygame

Window.size = (360, 640)

apology_msgs = [
    "\U0001F494 Dear sister, I know the prank I played hurt you. I'm really sorry. You're not just a friend, you're the heart my soul chose. ❤️ Please forgive your silly brother. 🙏",
    "\U0001F622 I know I crossed the line. You're one of the most precious people in my life. Your smile means everything to me. Please forgive me. 🤗",
    "\U0001F622 The prank was stupid. I'm ashamed for hurting you. I promise to never let this happen again. I miss your smile! \U0001F495",
    "\U0001F4EC You may not be my sister by blood, but you're my strength. I'm truly sorry. Please forgive me. ⬜"
]

class HomeScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        app.play_music()
        app.animate_home_screen(self)

class MainScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        app.play_music()
        app.animate_form_fields(self)

class ThankYouScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        app.play_music()
        app.animate_thankyou(self)

class SisterApp(MDApp):
    def build(self):
        pygame.mixer.init()
        self.music_path = "hindi_song.mp3"
        Builder.load_string(KV)
        self.logo_clicks = 0
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(ThankYouScreen(name="thankyou"))
        Clock.schedule_once(lambda dt: self.check_memories(sm.get_screen("thankyou")), 1)
        return sm

    def play_music(self):
        if os.path.exists(self.music_path):
            sound = pygame.mixer.Sound(self.music_path)
            sound.play()

    def check_memories(self, screen):
        if os.path.exists("memories") and os.listdir("memories"):
            screen.ids.see_memories.opacity = 1

    def animate_home_screen(self, screen):
        if hasattr(screen.ids, 'title_label'):
            anim1 = Animation(opacity=1, duration=1, t='out_quad') + Animation(pos_hint={"center_y": 0.9}, duration=0.4)
            anim1.start(screen.ids.title_label)

    def animate_form_fields(self, screen):
        for i, widget in enumerate([
            screen.ids.name_input,
            screen.ids.answer_input,
            screen.ids.submit_btn
        ]):
            widget.opacity = 0
            Clock.schedule_once(lambda dt, w=widget: Animation(opacity=1, duration=0.5, t='out_back').start(w), i * 0.3)

    def animate_thankyou(self, screen):
        card = screen.ids.thank_card
        card.opacity = 0
        card.size_hint = (0.1, 0.1)
        anim = Animation(opacity=1, size_hint=(0.9, 0.4), duration=1.2, t='out_elastic')
        anim.start(card)

    def get_apology(self):
        return random.choice(apology_msgs)

    def save_reply(self, name, message):
        if not os.path.exists("replies"):
            os.makedirs("replies")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(f"replies/{name}_reply.txt", "a") as f:
            f.write(f"{now} - {name}: {message}\n")

    def open_memories_folder(self):
        folder_path = os.path.abspath("memories")
        os.makedirs(folder_path, exist_ok=True)
        webbrowser.open(folder_path)

    def increment_logo_click(self):
        self.logo_clicks += 1
        if self.logo_clicks == 3:
            self.upload_images()
        elif self.logo_clicks == 4:
            self.show_replies()
        elif self.logo_clicks == 5:
            self.delete_memories()
        elif self.logo_clicks == 6:
            self.delete_replies()

    def upload_images(self):
        content = FileChooserIconView()
        popup = Popup(title="🎁 Opening Gift Box...", content=content, size_hint=(0.9, 0.9))
        def select(*args):
            files = content.selection
            if files:
                os.makedirs("memories", exist_ok=True)
                for f in files:
                    shutil.copy(f, "memories")
                popup.dismiss()
        content.bind(on_submit=lambda x, y, z: select())
        popup.open()

    def show_replies(self):
        content = BoxLayout(orientation="vertical")
        scroll = Label(size_hint_y=None)
        scroll.bind(texture_size=scroll.setter('size'))
        output = ""
        if os.path.exists("replies"):
            for file in os.listdir("replies"):
                with open(os.path.join("replies", file), "r") as f:
                    output += f.read() + "\n"
        scroll.text = output or "No replies found."
        content.add_widget(scroll)
        btn = Button(text="Close", size_hint_y=None, height=50)
        content.add_widget(btn)
        popup = Popup(title="📨 Opening Apology Letter...", content=content, size_hint=(0.9, 0.9))
        btn.bind(on_release=popup.dismiss)
        popup.open()

    def delete_memories(self):
        if os.path.exists("memories"):
            try:
                shutil.rmtree("memories")
            except PermissionError:
                print("Permission denied: close any image viewer and try again.")

    def delete_replies(self):
        content = BoxLayout(orientation="vertical")
        tf = MDTextField(hint_text="Enter password")
        btn = MDRaisedButton(text="Delete")
        content.add_widget(tf)
        content.add_widget(btn)
        popup = Popup(title="Enter Password to Delete", content=content, size_hint=(0.8, 0.4))
        def verify(instance):
            if tf.text == "kunal0709":
                shutil.rmtree("replies", ignore_errors=True)
                popup.dismiss()
        btn.bind(on_release=verify)
        popup.open()

KV = '''
ScreenManager:
    HomeScreen:
    MainScreen:
    ThankYouScreen:

<HomeScreen>:
    name: "home"
    MDFloatLayout:
        md_bg_color: 1, 0.95, 0.96, 1

        Image:
            id: logo_img
            source: "ak_logo.png"
            size_hint: 0.18, 0.18
            pos_hint: {"x":0.03, "top":0.98}
            allow_stretch: True
            on_touch_down:
                app.increment_logo_click()

        MDLabel:
            id: title_label
            text: "\U0001F496 Sorry My Sister \U0001F496"
            halign: "center"
            pos_hint: {"center_y": 0.93}
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 1, 0, 0.5, 1

        MDRaisedButton:
            text: "Start Apology \U0001F48C"
            pos_hint: {"center_x":0.5, "center_y":0.4}
            md_bg_color: 1, 0.5, 0.7, 1
            on_release:
                root.manager.current = "main"

<MainScreen>:
    name: "main"
    MDFloatLayout:
        MDTextField:
            id: name_input
            hint_text: "Enter your name"
            size_hint_x: 0.8
            pos_hint: {"center_x":0.5, "center_y":0.75}

        MDTextField:
            id: answer_input
            hint_text: "Why are you upset with me? \U0001F494"
            multiline: True
            size_hint_x: 0.8
            pos_hint: {"center_x":0.5, "center_y":0.6}

        MDRaisedButton:
            id: submit_btn
            text: "Send My Apology \U0001F64F"
            pos_hint: {"center_x":0.5, "center_y":0.45}
            md_bg_color: 1, 0.5, 0.7, 1
            on_release:
                app.save_reply(name_input.text, answer_input.text)
                root.manager.get_screen("thankyou").ids.msg.text = app.get_apology()
                root.manager.current = "thankyou"

<ThankYouScreen>:
    name: "thankyou"
    MDFloatLayout:
        MDCard:
            id: thank_card
            pos_hint: {"center_x":0.5, "center_y":0.6}
            size_hint: 0.9, 0.4
            md_bg_color: 1, 1, 1, 0.9
            elevation: 10
            radius: [20, 20, 20, 20]

            MDLabel:
                id: msg
                text: ""
                halign: "center"
                theme_text_color: "Primary"
                font_style: "Body1"

        MDRaisedButton:
            id: see_memories
            text: "\U0001F4F7 See Memories"
            pos_hint: {"center_x":0.5, "center_y":0.25}
            opacity: 0
            on_release:
                app.open_memories_folder()

        MDRaisedButton:
            text: "\U0001F500 Go Back"
            pos_hint: {"center_x":0.5, "center_y":0.1}
            on_release:
                root.manager.current = "home"
'''

if __name__ == "__main__":
    SisterApp().run()
