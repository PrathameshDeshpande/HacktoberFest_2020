#include "bits/stdc++.h"
#include "ext/pb_ds/assoc_container.hpp"
#include "ext/pb_ds/tree_policy.hpp"
using namespace std;
using namespace __gnu_pbds;

template<class T>
using ordered_set = tree<T, null_type,less<T>, rb_tree_tag,tree_order_statistics_node_update> ;

template<class key, class value, class cmp = std::less<key>>
using ordered_map = tree<key, value, cmp, rb_tree_tag, tree_order_statistics_node_update>;
// find_by_order(k)  returns iterator to kth element starting from 0;
// order_of_key(k) returns count of elements strictly smaller than k;

struct custom_hash { // Credits: https://codeforces.com/blog/entry/62393
    static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

template<class T> ostream& operator<<(ostream &os, vector<T> V) {
    os << "[ ";
    for(auto v : V) os << v << " ";
    return os << "]";
}
template<class T> ostream& operator<<(ostream &os, set<T> S){
    os << "{ ";
    for(auto s:S) os<<s<<" ";
    return os<<"}";
}
template<class T> ostream& operator<<(ostream &os, unordered_set<T> S){
    os << "{ ";
    for(auto s:S) os<<s<<" ";
    return os<<"}";
}
template<class T> ostream& operator<<(ostream &os, ordered_set<T> S){
    os << "{ ";
    for(auto s:S) os<<s<<" ";
    return os<<"}";
}
template<class L, class R> ostream& operator<<(ostream &os, pair<L,R> P) {
    return os << "(" << P.first << "," << P.second << ")";
}
template<class L, class R> ostream& operator<<(ostream &os, map<L,R> M) {
    os << "{ ";
    for(auto m:M) os<<"("<<m.first<<":"<<m.second<<") ";
    return os<<"}";
}
template<class L, class R> ostream& operator<<(ostream &os, unordered_map<L,R> M) {
    os << "{ ";
    for(auto m:M) os<<"("<<m.first<<":"<<m.second<<") ";
    return os<<"}";
}
template<class L, class R, class chash = std::hash<R> > ostream& operator<<(ostream &os, gp_hash_table<L,R,chash> M) {
    os << "{ ";
    for(auto m:M) os<<"("<<m.first<<":"<<m.second<<") ";
    return os<<"}";
}

#define TRACE
#ifdef TRACE
    #define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
    template <typename Arg1>
    void __f(const char* name, Arg1&& arg1){
        cerr << name << " : " << arg1 << endl;
    }
    template <typename Arg1, typename... Args>
    void __f(const char* names, Arg1&& arg1, Args&&... args){
        const char* comma = strchr(names + 1, ',');
        cerr.write(names, comma - names) << " : " << arg1<<" | ";
        __f(comma+1, args...);
    }
#else
    #define trace(...) 1
#endif

mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

inline int64_t random_long(long long l,long long r){
    uniform_int_distribution<int64_t> generator(l,r);
    return generator(rng);
}
inline int64_t random_long(){
    uniform_int_distribution<int64_t> generator(LLONG_MIN,LLONG_MAX);
    return generator(rng);
}


/*/---------------------------Defines----------------------/*/
typedef vector<int> vi;
typedef pair<int,int> pii;

#define ll long long
#define F first
#define S second
#define pb push_back
#define endl "\n"
#define all(v) (v).begin(),(v).end()
/*/-----------------------Modular Arithmetic---------------/*/

inline int add(int x,int y,int mod){
    x+=y;
    if (x>=mod) return x-mod;
    return x;
}
inline int sub(int x,int y,int mod){
    x-=y;
    if (x<0) return x+mod;
    return x;
}
inline int mul(int x,int y,int mod){
    return (x*1ll*y)%mod;
}
inline int power(int x,int y,int mod){
    int ans=1;
    while(y){
        if (y&1) ans=mul(ans,x,mod);
        x=mul(x,x,mod);
        y>>=1;
    }
    return ans;
}
inline int inv(int x,int mod){
    return power(x,mod-2,mod);
}
/*/-----------------------------Code begins----------------------------------/*/

const int mod1 = (ll)1e9+7;
const int mod2 = (ll)1e9+9;
const int N = 1e5+100;
ll hashs[N][2];
const int mod[2] = {mod1,mod2};
const int base = 31;

const int inv_b[2] = {inv(base,mod[0]),inv(base,mod[1])};

ll po[N][2];
ll invr[N][2];
void pre(){
	po[0][0]=1;
	po[0][1]=1;

	for(int i=1;i<N;++i){
		for(int j=0;j<2;++j){
			po[i][j]= (po[i-1][j]*1ll*base)%mod[j];
		}
	}
	invr[0][0]=1;
	invr[0][1]=1;

	for(int i=1;i<N;++i){
		for(int j=0;j<2;++j){
			invr[i][j]= (invr[i-1][j]*1ll*inv_b[j])%mod[j];
		}
	}
}

pair<ll,ll> get_hash(int i,int j){

	ll h1 = (hashs[j][0] - hashs[i-1][0] + mod[0])%mod[0];
	h1 = (h1*invr[i-1][0])%mod[0];

	ll h2 = (hashs[j][1] - hashs[i-1][1] + mod[1])%mod[1];
	h2 = (h2*invr[i-1][1])%mod[1];
	return {h1,h2};
}

void solve(){
    string s;
    cin>>s;

    int n=s.size();

    for(int i=1;i<=n;++i){
    	int z= s[i-1]-'a'+1;
    	for(int j=0;j<2;++j){
    		hashs[i][j]=(hashs[i-1][j] + po[i][j]*z)%mod[j];
    	}
    }
    long long cnt =0;
    for(int i=2;i<n;i+=2){
    	int j = (i+n)/2;
    	if (get_hash(1,i/2) == get_hash(i/2+1,i) && get_hash(i+1,j)==get_hash(j+1,n)){
    		 ++ cnt;
    	}
    }
    cout<<cnt<<endl;
}
int main(){
    // Use "set_name".max_load_factor(0.25);"set_name".reserve(512); with unordered set
    // Or use gp_hash_table<X,null_type>
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    cout<<fixed<<setprecision(25);
    int t=1;
    cin>>t;
    pre();
    while(t--) {
        solve();
    }
}
