def seocend_repeated_word(str1):
    str1=str1.split()
    count={}
    for i in str1:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    count_1=sorted(count.items(), key=lambda kv: kv[1])
    print(count_1)
    return count_1[-2]

print(seocend_repeated_word("it have important for skill also for life exprince skill skill"))
# def seocend_repeated_word(str1):
#     str1=list(str1.split())
#     temp={}
#     ls=[]
#     for i in str1:
#         if i in temp:
#             ls.append(i)
#         else:
#             temp[i]=0
#     return ls[1]
#
# print(seocend_repeated_word("it have important for skill also for life exprince skill skill"))
# print(seocend_repeated_word("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))