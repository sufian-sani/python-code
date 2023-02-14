pattern_str = "tadadattaetadadadafa"
pattern_required = "data"

# for i in pattern_str:
#     print(i,end=" ")
pattern_str_len=len(pattern_str)
pattern_required_len=len(pattern_required)

pattern_diff=int(pattern_str_len/pattern_required_len)

start_v=0
end_v = pattern_required_len
count = []
ls = []
loop_val = pattern_required_len
pattern_loop = pattern_diff
while loop_val >= 2:
    start_v = 0
    end_v = loop_val
    for i in range(pattern_loop):
        start_value = start_v
        end_value = end_v
        # print(end_value)
        # print(start_value, end_value)
        split_date = pattern_str[start_value:end_value]
        ls.append(split_date)
        start_v = end_value
        end_v = end_value + loop_val
    remainder_val = (pattern_str_len % loop_val)+1
    pattern_loop = int(pattern_str_len / loop_val) + remainder_val
    # print("long pattern:",pattern_loop)
    # print(pattern_loop)

    # o_count = 0
    # for i in ls:
    #     if i == pattern_required:
    #         o_count = o_count + 1
    #         count.append(o_count)

    loop_val = loop_val - 1

n_loop_val = pattern_required_len
ls_match = []
while n_loop_val >= 2:
    n_start_v = 0
    n_end_v = n_loop_val
    # print(end_value)
    # print(start_value, end_value)
    n_split_date = pattern_required[n_start_v:n_end_v]
    ls_match.append(n_split_date)
    n_loop_val = n_loop_val - 1

i_n_loop_val = pattern_required_len
i_n_loop_val_f = i_n_loop_val
i_n_start_v = 0
i_ls_match = []
while i_n_loop_val >= 2:
    i_n_start_v = i_n_start_v
    i_n_end_v = i_n_loop_val_f
    # print(end_value)
    # print(start_value, end_value)
    i_n_split_date = pattern_required[i_n_start_v:i_n_end_v]
    i_ls_match.append(i_n_split_date)
    i_n_start_v = i_n_start_v+1
    i_n_loop_val = i_n_loop_val - 1

print(ls_match)
print(i_ls_match)
mixed_ls=[]

[ls_match.append(x) for x in i_ls_match if x not in ls_match]

# print(ls_match)

ls_match = ls_match
# print(ls_match)

main_count_ls = []
for i in ls_match:
    for j in ls:
        if i==j:
            main_count_ls.append(i)
            # print(i, j)

final_new_menu = list(set(main_count_ls))

print(final_new_menu)
print(len(final_new_menu))

# print(main_count_ls)

# print(ls)
# print(ls_match)
# print(pattern_count)
# print(ls)
