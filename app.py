
import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc, Input, Output

# ==========================================
# CARGAR DATOS
# ==========================================

df = pd.read_csv("auto-mpg.csv")

# Imputar valores faltantes de horsepower
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())

# Crear característica adicional
df["power_to_weight"] = df["horsepower"] / df["weight"]


# ==========================================
# CREAR APLICACIÓN
# ==========================================

app = Dash(__name__)


# ==========================================
# GRÁFICAS INICIALES
# ==========================================

fig_cilindros = px.box(
    df,
    x="cylinders",
    y="mpg",
    title="Eficiencia de combustible según número de cilindros",
    labels={
        "cylinders": "Número de cilindros",
        "mpg": "Millas por galón (MPG)"
    }
)

fig_potencia_peso = px.scatter(
    df,
    x="power_to_weight",
    y="mpg",
    title="Relación entre potencia/peso y eficiencia de combustible",
    labels={
        "power_to_weight": "Relación potencia/peso",
        "mpg": "Millas por galón (MPG)"
    },
    trendline="ols"
)


# ==========================================
# OPCIONES DEL FILTRO
# ==========================================

opciones_cilindros = [
    {"label": "Todos", "value": "todos"}
]

for cilindros in sorted(df["cylinders"].unique()):
    opciones_cilindros.append({
        "label": f"{int(cilindros)} cilindros",
        "value": int(cilindros)
    })


# ==========================================
# INDICADORES
# ==========================================

promedio_mpg = df["mpg"].mean()
promedio_peso = df["weight"].mean()

# Resultados obtenidos durante el proceso de modelamiento
r2_modelo = 0.7368
mae_modelo = 3.1717


kpis = html.Div(
    [
        html.Div(
            [
                html.H4("MPG promedio"),
                html.H2(f"{promedio_mpg:.2f}")
            ],
            style={
                "padding": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "10px",
                "textAlign": "center",
                "width": "22%"
            }
        ),

        html.Div(
            [
                html.H4("Peso promedio"),
                html.H2(f"{promedio_peso:.2f}")
            ],
            style={
                "padding": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "10px",
                "textAlign": "center",
                "width": "22%"
            }
        ),

        html.Div(
            [
                html.H4("R² del modelo"),
                html.H2(f"{r2_modelo:.4f}")
            ],
            style={
                "padding": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "10px",
                "textAlign": "center",
                "width": "22%"
            }
        ),

        html.Div(
            [
                html.H4("MAE del modelo"),
                html.H2(f"{mae_modelo:.4f}")
            ],
            style={
                "padding": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "10px",
                "textAlign": "center",
                "width": "22%"
            }
        )
    ],
    style={
        "display": "flex",
        "justifyContent": "space-between",
        "marginBottom": "30px"
    }
)


# ==========================================
# DISEÑO DEL DASHBOARD
# ==========================================

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Dashboard de eficiencia de combustible",
                    style={
                        "margin": "0",
                        "fontSize": "32px"
                    }
                ),

                html.P(
                    "Análisis del conjunto de datos Auto MPG",
                    style={
                        "marginTop": "8px",
                        "fontSize": "16px"
                    }
                )
            ],
            style={
                "padding": "25px",
                "borderRadius": "12px",
                "marginBottom": "25px"
            }
        ),

        kpis,

        html.Div(
            [
                html.H3("Explorar por número de cilindros"),

                dcc.Dropdown(
                    id="filtro-cilindros",
                    options=opciones_cilindros,
                    value="todos",
                    clearable=False
                )
            ],
            style={
                "padding": "20px",
                "borderRadius": "12px",
                "marginBottom": "25px"
            }
        ),

        html.Div(
            [
                dcc.Graph(id="grafica-peso-mpg")
            ],
            style={
                "padding": "10px",
                "borderRadius": "12px",
                "marginBottom": "20px"
            }
        ),

        html.Div(
            [
                dcc.Graph(
                    id="grafica-cilindros-mpg",
                    figure=fig_cilindros
                )
            ],
            style={
                "padding": "10px",
                "borderRadius": "12px",
                "marginBottom": "20px"
            }
        ),

        html.Div(
            [
                dcc.Graph(
                    id="grafica-potencia-peso",
                    figure=fig_potencia_peso
                )
            ],
            style={
                "padding": "10px",
                "borderRadius": "12px",
                "marginBottom": "20px"
            }
        ),

        html.Div(
            [
                html.H3("Interpretación de los resultados"),

                html.P(
                    "Los resultados muestran una relación negativa entre "
                    "el peso de los vehículos y su eficiencia de combustible. "
                    "Además, la característica power_to_weight permitió "
                    "mejorar el desempeño predictivo del modelo."
                )
            ],
            style={
                "padding": "25px",
                "borderRadius": "12px",
                "marginTop": "20px"
            }
        )
    ],

    style={
        "maxWidth": "1200px",
        "margin": "auto",
        "padding": "30px",
        "fontFamily": "Arial",
        "backgroundColor": "#f5f6f8"
    }
)


# ==========================================
# CALLBACK
# ==========================================

@app.callback(
    Output("grafica-peso-mpg", "figure"),
    Input("filtro-cilindros", "value")
)

def actualizar_grafica(cilindros_seleccionados):

    if cilindros_seleccionados == "todos":

        datos_filtrados = df.copy()

        titulo = (
            "Relación entre peso y eficiencia de combustible"
        )

    else:

        datos_filtrados = df[
            df["cylinders"] == cilindros_seleccionados
        ]

        titulo = (
            f"Relación entre peso y eficiencia - "
            f"{cilindros_seleccionados} cilindros"
        )

    nueva_figura = px.scatter(
        datos_filtrados,
        x="weight",
        y="mpg",
        title=titulo,
        labels={
            "weight": "Peso del vehículo",
            "mpg": "Millas por galón (MPG)"
        },
        trendline="ols"
    )

    return nueva_figura


# ==========================================
# EJECUTAR APLICACIÓN
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
