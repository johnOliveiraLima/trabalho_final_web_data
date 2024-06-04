import streamlit as st
import pandas as pd
import plotly.express as px

st.write('João Vitor Lima de Oliveira - 2302736')
st.write('Camila Sampaio - 2302758')

st.title('''**Séries IMDB**''')

df = pd.read_csv('./1_bases_tratadas/notasSeriesTratado.csv', sep=';', encoding='utf-8')


with st.sidebar:
    logo_path = 'logoApp.png'
    st.image(logo_path)
    st.image(logo_path, width=250, use_column_width=True)

    st.title('Escolha uma série')

    st.write('As 100 séries mais bem-avaliadas do IMDB')

    st.write('Mas o que é o **IMDB**?')

    st.write('_"O IMDb é a fonte mais popular e confiável de conteúdos para filmes, TV e o mundo das celebridades"_ - **Amazon**')

    st.sidebar.subheader('Lista de Séries')

    titulo = st.selectbox(
    "Qual título deseja pesquisar?",
    df['titulo'],
    index=None,
    placeholder="Selecione o título da série...",
    )
    serie_selecionada = df[df['titulo'] == titulo]

    st.sidebar.subheader('Filtros de Busca')

    ano_lancamento = st.sidebar.slider('Ano de Lançamento:',
                    min_value=int(df['estreia'].min()),
                    max_value=int(df['estreia'].max()),
                    value=(int(df['estreia'].min()),
                    int(df['estreia'].max())))

    nota = st.sidebar.slider('Nota:',
                    min_value=float(df['nota'].min()),
                    max_value=float(df['nota'].max()),
                    value=(float(df['nota'].min()),
                    float(df['nota'].max())))
    
    st.write('**Classificações Indicativas**')
    livre = st.checkbox("Livre")
    mais10 = st.checkbox("+ 10")
    mais12 = st.checkbox("+ 12")
    mais14 = st.checkbox("+ 14")
    mais16 = st.checkbox("+ 16")
    mais18 = st.checkbox("+ 18")


    episodios = st.sidebar.slider('Número de episódios',
                    min_value=int(df['no_episodios'].min()),
                    max_value=int(df['no_episodios'].max()),
                    value=(int(df['no_episodios'].min()),
                    int(df['no_episodios'].max())))
    
    if st.button("Encontrar", type="primary"):
        filtros = df[
            (df['estreia'] >= ano_lancamento[0]) & 
            (df['estreia'] <= ano_lancamento[1]) &
            (df['nota'] >= nota[0]) &
            (df['nota'] <= nota[1]) &
            (df['no_episodios'] >= episodios[0]) &
            (df['no_episodios'] <= episodios[1])
        ]
        
        classificacoes = []
        if livre:
            classificacoes.append("Livre")
        if mais10:
            classificacoes.append("+ 10")
        if mais12:
            classificacoes.append("+ 12")
        if mais14:
            classificacoes.append("+ 14")
        if mais16:
            classificacoes.append("+ 16")
        if mais18:
            classificacoes.append("+ 18")
        
        if classificacoes:
            filtros = filtros[filtros['classificacao'].isin(classificacoes)]
        
        # Exibir os resultados filtrados
        st.write("Séries encontradas:")
        st.table(filtros)


st.write("**Informações sobre a série:** _selecione uma série..._")
st.table(serie_selecionada)

grouped_df = df.groupby(['estreia', 'classificacao'])['nota'].mean().reset_index()

fig = px.density_heatmap(
    grouped_df, 
    x='estreia', 
    y='classificacao', 
    z='nota', 
    histfunc='avg', 
    title='Notas por Classificação ao longo dos Anos',
    labels={'nota': 'Nota Média', 'estreia': 'Ano de Lançamento', 'classificacao': 'Classificação'},
    color_continuous_scale='Viridis',
    nbinsx=20,  
    nbinsy=10,  
)
fig.update_layout(
    xaxis_title='Ano de Lançamento',
    yaxis_title='Classificação',
    coloraxis_colorbar=dict(
        title="Nota Média"
    ),
    font=dict(
        size=12
    )
)



st.plotly_chart(fig)


fig2 = px.violin(df.nota)
st.plotly_chart(fig2)

fig3 = px.scatter(df,'estreia','no_episodios')
st.plotly_chart(fig3)

fig4 = px.pie(df, 'classificacao')
st.plotly_chart(fig4)

st.title('Indicadores Gerais')

col1,col2,col3 = st.columns(3)
col1.metric('Nota média',value=round(df.nota.mean(), 2))
col2.metric('Média de episódios',value=round(df.no_episodios.mean(), 2))
col3.metric('Média de avaliações',value=df.no_avaliacoes.mean())

col1,col2 = st.columns(2)
df2 = df.groupby('classificacao')[['nota']].count().reset_index().rename(columns={'nota':'no_avaliacoes'})
print(df2)
figpiz = px.pie(data_frame=df2,values='no_avaliacoes',names='classificacao')




