import datetime
import sys


if __name__ == "__main__":
    problem_name = sys.argv[1]
    lang = sys.argv[2]

    # create a file for each problem and write in it a template
    if lang == "cpp":
        file = open(problem_name + ".cpp", "w")
        file.write(
            """
/*

Problem: %s
Date: %s
By: Mouad BERQIA

*/
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace std;
using namespace __gnu_pbds;
#pragma GCC optimize("O2")
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> indexed_set;

typedef long long ll;
#define YES cout << "YES\\n"
#define NO cout << "NO\\n"
#define sz(c) (ll) c.size()
#define all(c) c.begin(), c.end()
#define MOD 1000000007

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);


    return 0;
}

"""
            % (problem_name, datetime.datetime.now().strftime("%d/%m/%Y"))
        )
        file.close()
    elif lang == "python":
        file = open(f"{problem_name}.py", "w")
        file.write(
            """
# Problem: %s
# Date: %s


# put your template python code here

"""
            % (problem_name, datetime.datetime.now().strftime("%d/%m/%Y"))
        )
        file.close()
