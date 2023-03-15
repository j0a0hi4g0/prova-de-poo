import classe_teste


#criando um objeto do tipo filme chamado: os vingadores
um_filme_qualquer = classe_teste.Filme("os vingadores",142)
um_filme_qualquer.exibir_duracao_em_horas()



#criando outro objeto (meu filme favorito) chamado: interestelar
meu_filme_favorito = classe_teste.Filme("os carros",100)

#fazendo alteração para a duração correta do filme interestelar 
meu_filme_favorito.duracao_em_minutos = 117

#exibindo novamente o filme interestelar com a duração correta
meu_filme_favorito.exibir_duracao_em_horas()

#um print mostrando os filmes em catálogo
print(f"Os filmes no catálogo são {um_filme_qualquer.titulo} e {meu_filme_favorito.titulo}")
