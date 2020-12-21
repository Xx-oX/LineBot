from fsm import TocMachine

machine = TocMachine(
    states=["user", "intro", "fsm", "menu", "write", "read", "change", "write_content", "read_show", "change_select", "change_content"],
    transitions=[
        {
            "trigger": "advance",
            "source": ["menu", "user"],
            "dest": "intro",
            "conditions": "is_going_to_intro",
        },
        {
            "trigger": "advance",
            "source": ["menu", "user"],
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "write",
            "conditions": "is_going_to_write",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "read",
            "conditions": "is_going_to_read",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "change",
            "conditions": "is_going_to_change",
        },
        {
            "trigger": "advance",
            "source": "write",
            "dest": "write_content",
            "conditions": "is_going_to_write_content",
        },
        {
            "trigger": "advance",
            "source": "read",
            "dest": "read_show",
            "conditions": "is_going_to_read_show",
        },
        {
            "trigger": "advance",
            "source": "read_show",
            "dest": "read",
            "conditions": "is_going_back_to_read",
        },
        {
            "trigger": "advance",
            "source": "change",
            "dest": "change_select",
            "conditions": "is_going_to_change_select",
        },
        {
            "trigger": "advance",
            "source": "change_select",
            "dest": "change_content",
            "conditions": "is_going_to_change_content",
        },
        {
            "trigger": "advance",
            "source": ["menu", "write", "read", "change", "write_content", "read_show", "change_select", "change_content"],
            "dest": "menu",
            "conditions": "is_going_back_to_menu",
        },
        {"trigger": "go_back", "source": ["intro", "fsm", "menu"], "dest": "user"}
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

machine.get_graph().draw("fsm.png", prog="dot", format="png")