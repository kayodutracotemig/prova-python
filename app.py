import pandas as pd
df_tabela = pd.read_csv("censo_1872.csv")
df = df.drop_duplicates(homens_livres, homens_escravizados, mulheres_livres, mulheres_escravizadas)

soma_linhas = (homens_livres, homens_escravizados, mulheres_livres, mulheres_escravizadas)

percentual_homens_livres =  homens_livres / (homens_livres + homens_escravizados)
percentual_mulheres_livres =  mulheres_livres / (mulheres_livres + mulheres_escravizadas)
percentual_homens_escravizados =  homens_escravizados / (homens_livres + homens_escravizados)
percentual_mulheres_escravizadas =  mulheres_escravizadas / (mulheres_livres + mulheres_escravizadas)

st.title("Painel Percenbtual de escravizados")
st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela de escravizados")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos de escravizados")

st.subheader("5. Gráfico de Pizza")
    dados_pizza = pd.DataFrame([
        {percentual_homens_livres},
        {percentual_mulheres_livres},
        {percentual_homens_escravizados},
        {percentual_mulheres_escravizadas},
    ])

    fig_pizza = px.pie(
        dados_pizza,
        names="Total",
        values="IQVU",
        title="Proporção de escravizados",
        color="Total",
        template="plotly_dark"
    )
    fig_pizza.update_traces(textinfo="percent+label+value")
    fig_pizza.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_pizza, use_container_width=True)



