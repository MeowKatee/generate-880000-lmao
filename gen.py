import sys

def num_digits(num: int);
    digits = []
    tmp = num
    while (tmp != 0):
        digits.append(tmp % 10)
        tmp //= 10

    return digits

def gen_cpp(loop_num):          # {{{
    f = open("code.cpp", "w")
    f.write("""#include <iostream>
using namespace std;

int main()
{
    cout << "请给出一个不多于5位的正整数：";
    int x;
    cin >> x;

    switch (x) {
""")

    for num in range(1, loop_num):
        digits = num_digits(num)
        f.write("    case " + str(num) + ":\n")
        f.write("        cout << \"是" + str(len(digits)) + "位数\" << endl;\n")
        for i, d in enumerate(digits):
            pos = ["个", "十", "百", "千", "万"][i]
            f.write("        cout << \"" + pos + "位数是：" + str(d) + "\" << endl;\n")
        f.write("        cout << \"倒过来是：")
        for d in digits:
            f.write(str(d))
        f.write("\" << endl;\n")
        f.write("        break;\n")

    f.write("""    default:
        cout << "数字不合规！" << endl;
    }
}
""")
    f.close()
# }}}


def gen_c(loop_num):            # {{{
    f = open("code.c", "w")
    f.write("""#include <stdio.h>

int main()
{
    int x;
    printf("请给出一个不多于5位的正整数：");
    scanf("%d", &x);

    switch (x) {
""")

    for num in range(1, loop_num):
        digits = num_digits(num)
        f.write("    case " + str(num) + ":\n")
        f.write("        printf(\"是" + str(len(digits)) + "位数\\n\");\n")
        for i, d in enumerate(digits):
            pos = ["个", "十", "百", "千", "万"][i]
            f.write("        printf(\"" + pos + "位数是：" + str(d) + "\\n\");\n")
        f.write("        printf(\"倒过来是：")
        for d in digits:
            f.write(str(d))
        f.write("\\n\");\n")
        f.write("        break;\n")

    f.write("""    default:
        printf("数字不合规！\\n");
    }
}
""")
    f.close()
# }}}


def gen_py(loop_num):           # {{{
    f = open("code.py", "w", encoding="utf-8")
    f.write("""x = int( input("请给出一个不多于5位的正整数：") )
match x:
""")

    for num in range(1, loop_num):
        digits = num_digits(num)
        f.write("    case " + str(num) + ":\n")
        f.write("        print(\"是" + str(len(digits)) + "位数\")\n")
        for i, d in enumerate(digits):
            pos = ["个", "十", "百", "千", "万"][i]
            f.write("        print(\"" + pos + "位数是：" + str(d) + "\")\n")
        f.write("        print(\"倒过来是：")
        for d in digits:
            f.write(str(d))
        f.write("\")\n")

    f.write("""    case _:
        print("数字不合规！")
""")
    f.close()
# }}}

def gen_rs(loop_num):
    pass


def main():
    if len(sys.argv) in (2, 3):
        loop_num = int(sys.argv[2]) if len(sys.argv) == 3 else 100000
        target = sys.argv[1]
        if target == "c":
            gen_c(loop_num)
        elif target == "cpp":
            gen_cpp(loop_num)
        elif target == "py":
            gen_py(loop_num)
        else:
            sys.exit(f"ERROR: Unsupported target '{target}'")
    else:
        sys.exit("ERROR: Unmatched arguments")

if __name__ == "__main__":
    main()
