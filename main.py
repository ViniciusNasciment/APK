from flet import *
import flet as ft
from custom_checkbox import CustomCheckBox

def main (page: Page):
    BG = '#696969'  #000000 #708090
    FWG = '#97b4ff'
    FG = '#1C1C1C'
    PINK = '#FF8C00'

    circle = Stack(
    controls=[
      Container(
        width=100,
        height=100,
        border_radius=50,
        bgcolor='white12'
        ),
      Container(
                  gradient=SweepGradient(
                      center=alignment.center,
                      start_angle=0.0,
                      end_angle=3,
                      stops=[0.5,0.5],
                  colors=['#00000000', PINK],
                  ),
                  width=100,
                  height=100,
                  border_radius=50,
                  content=Row(alignment='center',
                      controls=[
                        Container(padding=padding.all(5),
                          bgcolor=BG,
                          width=90,height=90,
                          border_radius=50,
                          content=Container(bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                          content=CircleAvatar(opacity=0.8,
                foreground_image_url="https://avatars.githubusercontent.com/u/121808252?s=400&u=35e60e838a25c68121080f413338456341b2f448&v=4"
            )
                          )
                          )
                      ],
                  ),
              ),
      
    ]
  )

    

    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = transform.Scale(
            0.8,alignment=alignment.center_right)

        page_2.update()

    def resotore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(
            1,alignment=alignment.center_right)
        page_2.update()


    create_task_view = Container(
    content=Container(
        on_click=lambda _: page.go('/create_task'),  # Correção aqui
        height=40,
        width=40,
        content=Text('x')
    )
    )
    tasks = Column(
        height=400,
        scroll='auto',
       # controls=[
        # Container(height=50,width=300,bgcolor='red'),
         # Container(height=50,width=300,bgcolor='red'),
          # Container(height=50,width=300,bgcolor='red'),
           # Container(height=50,width=300,bgcolor='red')
       # ]
    )

    for i in range(10):
        tasks.controls.append(
          Container(
              height=70,
              width=400,
              bgcolor=BG,
              border_radius=25,padding=padding.only(
                  left=20,top=25,
              ),
              content=CustomCheckBox(
                  color=PINK,
                  size=25,
                  label='Crie conteúdo interessante!'
                  
              )),

        )

    categories_card = Row(
        scroll='auto'
    )
    categories = ['Negócios', 'Família', 'Amigos',]
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG,
                height=110,
                width=170,
                padding=15,
                content=Column(
                    controls=[
                        ft.Text('40 Tasks',color="white"),
                        Text(category,color="white"),
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white12",
                            border_radius=20,
                            padding=padding.only(right=i*30),
                             content=Container(
                                 bgcolor=PINK,
                             )
                        )
                    ]
                  
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                            content=Icon(
                                icons.MENU,color="#FF8C00")),
                                Row(
                                    controls=[
                                        Icon(icons.SEARCH,color="#FF8C00"),
                                        Icon(icons.NOTIFICATIONS_OUTLINED,color="#FF8C00"),
                                    ],
                                ),
                             ],
                        ),
                    
                    Text(
                        value='Bem Vindo\'s, Vinicius!',color="#FF8C00",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,weight='bold',font_family='poppins'
                    ),
                    Text(
                        value='Categorias',color="#FF8C00",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,weight='bold',font_family='poppins'
                    ),
                    Container(
                        padding=padding.only(top=10,bottom=20),
                        content=categories_card
                    ),
                    Container(height=20),
                    Text("Today's Tasks",color="#FF8C00",weight='bold',font_family='poppins'),
                    Stack(
                        controls=[
                            tasks,]
                            ##FloatingActionButton(
                               ## icon = icons.ADD,on_click=lambda _: route_change('/create_task'),
                               ## bgcolor=ft.colors.ORANGE,
                            )
                        ]
                    ),
                
    )
    
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "/fonts/OpenSans-Regular.ttf"}
    page.title = "Text theme styles"
    page.scroll = "adaptive"
   ## page.window_max_width = 400
   ## page.window_max_height = 750
    page.padding = 0
    page.floating_action_button = FloatingActionButton(
        icon=icons.ADD,
        on_click=lambda _: route_change('/create_task'),
        bgcolor=ft.colors.ORANGE,)



    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50,top=60,right=200),

        content=Column(
            controls=[
                Row(alignment='end',
                    controls=[
                Container(border_radius=25,
                          padding=padding.only(top=13,left=13),
                          height=50,
                          width=50,
                          border=border.all(color=PINK,width=1),
                          on_click=lambda e: resotore(e),
                          content=Text('<',color="#FF8C00",weight='bold')
                        )
                          ]
                        ),
                        Container(height=20),
                        circle,
                        Text('Vinicius\nEmidio',size=32,weight='bold'),
                        Container(height=20),
                        Row(controls=[
                            Icon(icons.FAVORITE_BORDER_SHARP,color="#FF8C00"),
                            Text('Templates',size=15,weight=FontWeight.W_300,color="#FF8C00",font_family='poppins')
                        ]),
                        Row(controls=[
                            Icon(icons.CARD_TRAVEL,color="#FF8C00"),
                            Text('Categorias',size=15,weight=FontWeight.W_300,color="#FF8C00",font_family='poppins')
                        ]),
                        Row(controls=[
                            Icon(icons.CALCULATE_OUTLINED,color="#FF8C00"),
                            Text('Analise',size=15,weight=FontWeight.W_300,color="#FF8C00",font_family='poppins')
                        ]),
                        Image(src=f"GRAFICO CERTO.png",
                              width=65,
                              height=65,),
                              Text('Good',color=FG,font_family='poppins',),
                              Text('Consistency',size=22,)
                    ]
                 )
            )
    
    page_2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,## PARTE DA FRENTE
                border_radius=35,
                animate=animation.Animation(680,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400,curve='decelerate'),
                padding=padding.only(
                    top=50,left=20,
                    right=20,bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                 ]
             )
                      
         )
     ]
 )

    container = Container(
    width=395,
    height=685,
    bgcolor=BG,
    border_radius=30,
    content=Stack(
        controls=[
            page_1,
            page_2,
        ]
      )
    )
    pages ={
        '/':View(
            "/",
            [
                container
            ],
        ),
        '/create_task': View(
                        "/create Task",
                        [
                            create_task_view
                        ]
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
     )
    page.go_route_change = route_change
    page.go(page.route)
    page.add(container)
    


    


app(target=main)

