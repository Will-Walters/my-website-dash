import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    children=[
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.NavbarBrand(dbc.NavLink("William H. Walters", href="/")),
                ],
                    width={"size": "auto"})
            ],
                align="center",
                className="g-0"),
            dbc.NavItem(dbc.NavLink("Resume", href="/resume")),
            dbc.NavItem(dbc.NavLink("Freelance", href="/freelance")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("1", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="Code Projects",
            ),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("About Me", header=True),
                    dbc.DropdownMenuItem("Bio", href="/bio"),
                    dbc.DropdownMenuItem("Photos", href="/myphotos"),
                ],
                nav=True,
                in_navbar=True,
                label="About Me",
            ),
        ])
    ],
    color="primary",
    dark=True,
    sticky="top"
)
