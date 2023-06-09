from tkinter import *
from dbd import *


#definindo algumas cors

co0 = "#000000"  # preta
co1 = "#59656F"
co2 = "#feffff"  # branca
co3 = "#FFD700"  # gold
co4 = "#FF6347"  # tomate
co5 = "#59b356"  # verde
co6 = "#cdd1cd"  # cizenta
co7 = "#DDA0DD"  #plum rose
co8 = "#ecc19c"   #bege
co9 = "#1e847f" #azul piscina
co10 ="#000000" #preto

##############Criando janela#########
janela=Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x225') #tamanho da janela do app
janela.title('To-do App')
janela.configure(background=co7)

#divisão da janela em partes
f_esquerda= Frame(janela, width= 300, height=200, bg=co9,relief='flat' )
f_esquerda.grid(row=0, column=0, sticky=NSEW) #parte da janela de afazers

f_direita= Frame(janela, width= 200, height=250, bg=co8,relief='flat' )
f_direita.grid(row=0, column=1, sticky=NSEW)# parte das terefas ja criadas

############ dividindo o frame da esquerda em duas partes####
fe_cima= Frame(f_esquerda, width=300, height=50, bg= co9, relief='flat')
fe_cima.grid(row=0,column=0, sticky=NSEW)

fe_baixo= Frame(f_esquerda, width=300, height=150, bg=co9, relief= "flat")
fe_baixo.grid(row=1, column=0, sticky= NSEW)

def main(a):
    ## novo ##
    if a =="novo":
        
        for widget in fe_baixo.winfo_children():
            widget.destroy()

        def adicionar():
            tarefa_entry= entry.get()
            inserir([tarefa_entry])
            mostrar()

        lb= Label(fe_baixo, text="Nova Tarefa", width=42, height=5, pady=15, padx=10, anchor=CENTER)
        lb.grid(row=0,column=0,sticky=NSEW)

        entry= Entry(fe_baixo, width=15)
        entry.grid(row=1, column=0, sticky=NSEW)

        b_add= Button(fe_baixo, text="ADD", width=9, pady=10, height=1, bg=co3, fg="white", font="8", anchor="center", relief=RAISED, command=adicionar)
        b_add.grid(row=2, column=0, sticky= NSEW, pady=1)

    ## atualizar ##
    if a == "atualizar":
        for widget in fe_baixo.winfo_children():
            widget.destroy()
        
        def on():
           


            lb= Label(fe_baixo, text="Atualizar Tarefa", width=42, height=5, pady=15, padx=10, anchor=CENTER)
            lb.grid(row=0,column=0,sticky=NSEW)

            entry= Entry(fe_baixo, width=15)
            entry.grid(row=1, column=0, sticky=NSEW)

            v_selecionado= listbox.curselection()[0]
            palavra= listbox.get(v_selecionado)
            entry.insert(0,palavra)

            tarefas= selecionar()

            def alterar():
                for item in tarefas:
                    if palavra==item[1]:
                        nova=[entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0, END)
                mostrar()

            b_alterar= Button(fe_baixo, text="Atualizar", width=9, pady=10, height=1, bg=co5, fg="white", font="8", anchor="center", relief=RAISED, command=alterar)
            b_alterar.grid(row=2, column=0, sticky= NSEW, pady=1)
        on()

#######remover fução#######
def remover():
    v_selecionado= listbox.curselection()[0]
    palavra= listbox.get(v_selecionado)
    tarefas= selecionar()

    for item in tarefas:
        if palavra == item[1]:
            deletar([item[0]])
    mostrar()

########## criando botoes novo, remover e atulizar ######
b_new= Button(fe_cima, text=" NEW", width=10, height=1, bg=co3, fg="white", font="5", anchor="center", relief="flat", command=lambda: main("novo"))
b_new.grid(row=0, column=0, sticky= NSEW, pady=1)

b_remove= Button(fe_cima, text=" REMOVE", width=10, height=1, bg=co4, fg="white", font="5", anchor="center", relief="flat", command=remover)
b_remove.grid(row=0, column=1, sticky= NSEW, pady=1)

b_edit= Button(fe_cima, text=" EDIT", width=10, height=1, bg=co5, fg="white", font="5", anchor="center", relief="flat", command=lambda: main("atualizar"))
b_edit.grid(row=0, column=2, sticky= NSEW, pady=1)


####### criando o Listbox and a label####
label= Label(f_direita, text="Tarefas", width=37, height=1, pady=7, padx=10, relief="flat", anchor=W, font=("Cournier 20 bold"), fg=co0, bg=co2)
label.grid(row=0,column=0,sticky=NSEW,pady=1)

listbox= Listbox(f_direita, font=("Courier 9 bold"), width=1)
listbox.grid(row=1, column=0, sticky= NSEW, pady=5)

#####adicionando itens nas terfas na listbox####
def mostrar():
    listbox.delete(0, END)
    tarefas= selecionar()
    for item in tarefas:
        listbox.insert(END,item[1])

mostrar()
# '''
# for item in tarefas:
#     listbox.insert(END, item)
# '''

janela.mainloop()