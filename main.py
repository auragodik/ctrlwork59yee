import flet as ft
from db import sqlbuys


def main(page: ft.Page):
    page.title = 'список покупок'
    page.theme_mode = ft.ThemeMode.DARK

    shops_list = ft.Column(spacing=10)
    filters = 'all'

    def load_shops():
        shops_list.controls.clear()
        for shops_id, shop_text, kupleno in sqlbuys.get_buys(filters):
            shops_list.controls.append(create_shop_list(shops_id, shop_text, kupleno))
        page.update()

    def create_shop_list(shops_id, shop_text, kupleno):
        task_field = ft.TextField(
            value=shop_text,
            read_only=True,
            expand=True
        )
        delete_button = ft.IconButton(
            icon=ft.Icons.DELETE, 
            on_click=lambda e, sid=shops_id: delete_shop(sid)
        )
        checkbox_buys = ft.Checkbox(
            value=bool(kupleno),
            on_change=lambda e: toggle_s(shops_id, e.control.value)
        )
        return ft.Row([checkbox_buys, task_field, delete_button])

    def toggle_s(shops_id, is_purchased):
        sqlbuys.update_buys(shops_id=shops_id, kupleno=int(is_purchased))
        load_shops()

    def add_buys(_):
        if shops_input.value:
            shops = shops_input.value
            shops_id = sqlbuys.add_buys(shops)
            shops_list.controls.append(create_shop_list(shops_id=shops_id, shop_text=shops, kupleno=0))
            shops_input.value = ""
            page.update()

    def delete_shop(shops_id):
        sqlbuys.delete_buys(shops_id)
        load_shops()

    def set_filters(filters_value):
        nonlocal filters
        filters = filters_value
        load_shops()

    filter_buttons = ft.Row([
        ft.ElevatedButton('все', on_click=lambda e: set_filters('all'), icon=ft.Icons.ALL_INBOX),
        ft.ElevatedButton('некупленные', on_click=lambda e: set_filters('unpurchased'), icon=ft.Icons.STOP_OUTLINED),
        ft.ElevatedButton('купленные', on_click=lambda e: set_filters('purchased'), icon=ft.Icons.CHECK_BOX)
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    shops_input = ft.TextField(label='что желаете купить??', expand=True, on_submit=add_buys)
    buys_button = ft.ElevatedButton('ADD', on_click=add_buys)
    page.add(ft.Row([shops_input, buys_button]), filter_buttons, shops_list)

    load_shops()


if __name__ == '__main__':
    sqlbuys.init_db()
    ft.app(target=main)
