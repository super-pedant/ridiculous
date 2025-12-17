import streamlit as st
import random
import string

count=0
kansoku=0
#英語の小文字
mozi=string.ascii_lowercase
#数字
num=string.digits
kari=[]
hontai=[]
kotoba=st.text_input("言葉を入力して")
moziretu=st.text_input("復号できるよ")
fukugou=[]
max=100000



def main():
    global hontai
    global kansoku
    kansoku=0
    hontai=[]
    for p in range(max):       
        angou()
        kaidoku()
        if fukugou and kansoku<len(kotoba):
            if fukugou[0]==kotoba[kansoku]:
                #一文字分ずつ、暗号を確定させていく
                kansoku=kansoku+1
                hontai.extend(kari)
            if kansoku>=len(kotoba):
                break
    if p>=max:
        st.write("暗号化失敗")
    else:
        st.write("暗号: " + "".join(hontai) + "".join(random.choices(mozi, k=random.randint(0,6))))


st.title("言葉暗号化アプリ")
st.write("Hello, World!")
st.image("computer_hacker_black1.png")

def kaidoku():
    count=0
    global fukugou
    fukugou=[]
    for i in range(len(kari)):
        if i < len(kari) and kari[i] in num:
            #数字から数字への距離と数値を掛けた値がアルファベットに変換される
            fukugou.append(mozi[count*(int(kari[i]))%26])
            count=0
            break
        else:
            count=count+1

def kaidokuA(array):
    count=0
    global fukugou
    fukugou=[]
    i=0
    while i < len(array):
        if array[i] in num:
            fukugou.append(mozi[count*(int(array[i]))%26])
            count=0
            i=i+1
        else:
            count=count+1
            i=i+1
    st.write("復号結果: "+"".join(fukugou))


def angou():
    global kari
    kari=[]
    #ランダムに文字と数字を生成
    for q in range(len(kotoba)*10):
        tango=random.choice(mozi+num)
        kari.append(tango)
        if tango in num:
            break
    

if kotoba: 
    main()
elif moziretu:
    kaidokuA(moziretu)
else:
    pass