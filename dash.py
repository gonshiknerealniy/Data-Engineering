from dash import Dash, dcc, html

database = "synthesis.db"
conn = sqlite3.connect(database)

cursor = conn.cursor()

table_name = "synthesis"
cursor.execute(f'SELECT * FROM {"information"}')
rows = cursor.fetchall()

columns = [description[0] for description in cursor.description]
data = pd.DataFrame(rows, columns=columns)

cursor.close()
conn.close()

# Создание веб-приложения Dash
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Data Visualization"),
        dcc.Graph(
            id="graph",
            figure=px.scatter(
                data,
                x="API",
                y="liq_amount_mL",
                title="Visualization of Data from SQLite",
            ),
        ),
    ]
)

# Запуск приложения
if __name__ == "__main__":
    app.run_server(debug=True)
