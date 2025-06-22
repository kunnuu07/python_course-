from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import pyttsx3
import random
import os

Window.size = (400, 700)

class SisterApologyApp(MDApp):
    tap_count = 0

    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Light"

        self.anooy = random.choice([
            "Sleeping Beauty", "Chatterbox", "Miss Always Right",
            "Mood Swing Machine", "Snack Stealer"
        ])
        self.taide = random.choice([
            "Dear sister, I know the prank I played hurt you, and for that, I'm truly sorry...",
            "I know I crossed the line with my prank, and I regret it deeply...",
            "My dear sister, I'm sorry from the deepest corner of my heart...",
            "I know I messed up, and it hurts knowing you're upset with me..."
        ])

        # Main screen with FloatLayout for layers
        self.screen = MDScreen()
        self.layout = FloatLayout()

        # Background Image
        self.bg = Image(source="background.jpg", allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.bg)

        # Top App Bar
        self.topbar = MDTopAppBar(
            title="Sister 💕",
            pos_hint={"top": 1},
            elevation=4,
            md_bg_color=(1, 0.7, 0.8, 1),
            on_title_press=self.hidden_access
        )
        self.layout.add_widget(self.topbar)

        # Main content in a vertical box layout
        vbox = MDBoxLayout(orientation="vertical", spacing=15, padding=20,
                           size_hint=(0.9, None), height=600, pos_hint={"center_x": 0.5, "center_y": 0.47})

        # Heart animation
        self.heart = MDIconButton(
            icon="heart",
            theme_icon_color="Custom",
            icon_color=(1, 0.3, 0.5, 1),
            icon_size="60sp",
            pos_hint={"center_x": 0.5}
        )
        heart_anim = Animation(opacity=0.2, duration=0.6) + Animation(opacity=1, duration=0.6)
        heart_anim.repeat = True
        heart_anim.start(self.heart)

        # Card with inputs
        self.card = MDCard(orientation="vertical", padding=20, spacing=15,
                           md_bg_color=(1, 1, 1, 0.9),
                           radius=[20, 20, 20, 20],
                           size_hint=(1, None), height=420)

        self.name_input = MDTextField(
            hint_text=f"Enter your name, dear {self.anooy}",
            helper_text="She’ll see this 💌",
            icon_right="account",
            size_hint_x=None,
            width=300,
            pos_hint={"center_x": 0.5}
        )

        self.ans_input = MDTextField(
            hint_text="Why are you upset?",
            helper_text="I really want to know 🥺",
            icon_right="emoticon-sad-outline",
            multiline=True,
            size_hint_x=None,
            width=300,
            pos_hint={"center_x": 0.5}
        )

        self.submit_btn = MDRaisedButton(
            text="Send Apology 💌",
            pos_hint={"center_x": 0.5},
            on_release=self.handle_submit
        )

        self.result_label = MDLabel(
            text="Hey, what happened?\nWhy are you upset with me?",
            halign="center",
            theme_text_color="Secondary",
            opacity=0
        )

        self.card.add_widget(self.name_input)
        self.card.add_widget(self.ans_input)
        self.card.add_widget(self.submit_btn)
        self.card.add_widget(self.result_label)

        # Add heart and card to layout
        vbox.add_widget(self.heart)
        vbox.add_widget(self.card)

        self.layout.add_widget(vbox)
        self.screen.add_widget(self.layout)

        # Welcome speech
        self.speak("Hey, what happened? Why are you upset with me?")
        return self.screen

    def speak(self, text):
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 140)
            engine.setProperty('volume', 1.0)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print("TTS error:", e)

    def handle_submit(self, instance):
        name = self.name_input.text.strip()
        ans = self.ans_input.text.strip()
        if name and ans:
            self.result_label.text = self.taide
            self.save_to_file(name, ans)
            self.fade_in_apology()
            self.speak(self.taide)
        else:
            Snackbar(text="Please fill both fields 📝").open()

    def fade_in_apology(self):
        anim = Animation(opacity=1, duration=1.5)
        anim.start(self.result_label)

    def save_to_file(self, name, ans):
        fileName = name.upper() + "_sis_replay.txt"
        with open(fileName, "a", encoding="utf-8") as f:
            f.write(name + "\n")
            f.write(f"Answer of dear {name}:\n\t" + ans + "\n\n\n")

    def hidden_access(self, instance):
        self.tap_count += 1
        if self.tap_count == 3:
            self.show_secret()

    def show_secret(self):
        try:
            files = [f for f in os.listdir() if f.endswith("_sis_replay.txt")]
            content = ""
            for file in files:
                with open(file, "r", encoding="utf-8") as f:
                    content += f"\n📄 " + file + ":\n" + f.read()
            if content.strip() == "":
                content = "No replies yet."
            self.dialog = MDDialog(
                title="🛡️ Secret Replies",
                text=content,
                size_hint=(0.9, 0.9)
            )
            self.dialog.open()
        except Exception as e:
            Snackbar(text=f"Error: {e}").open()

if __name__ == '__main__':
    SisterApologyApp().run()
