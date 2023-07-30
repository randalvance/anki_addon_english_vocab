from aqt import gui_hooks, mw
from aqt.editor import Editor
from anki.cards import Card
from pprint import pprint as pp

def my_func(card: Card) -> None:
    assert mw is not None
    config = mw.addonManager.getConfig(__name__)
    print("Message from Randal!")
    assert config is not None
    print("var is", config['myvar'])

def on_editor_clicked(editor: Editor):
    print("Editor Button was clicked")

def register_editor_buttons(buttons: list[str], editor: Editor):
    btn = editor.addButton(None, "get_meaning", on_editor_clicked, "No Tip", "Some Label")
    buttons.append(btn)

gui_hooks.reviewer_did_show_answer.append(my_func)
gui_hooks.editor_did_init_buttons.append(register_editor_buttons)

