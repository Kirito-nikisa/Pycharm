import flet as ft


def main(page, years=None, study=None, free_time=None):

    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    years = ft.Ref[ft.TextField]()
    study = ft.Ref[ft.TextField]()
    free_time = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello,My name {first_name.current.value} {last_name.current.value}.I`m{years.current.value} "
                    f"years old.I study in {study.current.value}.In my free time I {free_time.current.value}.")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        years.current.value = ""
        study.current.value = ""
        free_time.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.TextField(ref=years, label="Years"),
        ft.TextField(ref=study, label="study"),
        ft.TextField(ref=free_time, label="free time"),


        ft.ElevatedButton(" Hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )

ft.app(target=main)