#include<iostream>
#include<vector>
using namespace std ;

constexpr int V_MAX = 205 ;

vector<int> edges[V_MAX] ;
bool visited[V_MAX] ;
int V, E ;
int component_num ; // connected component
string place_name[V_MAX] ;

void dfs(const int& cur, const int& ban_v){
  if(visited[cur] || cur==ban_v) return ;
  visited[cur] = true ;
  for(int i=0 ; i<edges[cur].size() ; i++){
    dfs(edges[cur][i], ban_v) ;
  }
}

int countComponentNum(const int ban_v=-1){
  for(int v=0 ; v<V ; v++) visited[v] = false ;
  component_num = 0 ;
  for(int v=0 ; v<V ; v++){
    if(ban_v==v || visited[v]) continue ;
    dfs(v, ban_v) ;
    component_num++ ;
  }
  return component_num ;
}

int main(){

  cout << "Please input the number of vertixes and edges:" << endl ;
  cout << "---------------------------------------------------------" << endl ;

  while(cin>>V>>E){
    cout << endl << "Please input the name of the places(in the order of the numbers):" << endl ;
    cin.get() ;
    for(int v=0 ; v<V ; v++){
      getline(cin, place_name[v]) ;
      edges[v].clear() ;
    }
    cout << "------------------------------------------------------" << endl ;
    cout << "Please input the map using numbers and the order of the places you input, please start form 0: " << endl ;
    int a, b ;
    for(int e=0 ; e<E ; e++){
      cin>>a>>b ;
      edges[a].push_back(b) ;
      edges[b].push_back(a) ;
    }
    // finding articulation vertex
    if(countComponentNum()>1){
      cout << "This graph is not connected." << endl ;
      continue ;
    }
    bool a_point_found = false ;
    for(int v=0 ; v<V ; v++){
      int component_num = countComponentNum(v) ;
      if(component_num>1){
        cout << place_name[v] << " is an articulation point. It separates the graph into " << component_num << " components." << endl ;
        a_point_found = true ;
      }
    }
    if(!a_point_found) cout << "There is no articulation point in this graph." << endl ;
  }
  return 0 ;
}


/*
http://web.ntnu.edu.tw/~algo/Component.html
31 55
Far East
West Coast of North America
East Coast of North America
Caribbean
West Coast of South America
Indian
South-East Asia
Australia
New Zealand
East Africa
Mediterranean Sea
North-west Europe
Cape of Good Hope
West Africa
North of Indian Ocean
Asia Pacific
Europe
Persian Gulf
West Europe
Suez Canal
Gibraltar
Indian Ocean
Central South Africa
East Coast of South America
Japan
California
Seattle
Vancouver
New York
United Kingdom
Great Lakes
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 10
0 16
2 3
2 20
6 9
6 10
6 12
6 24
8 1
8 2
10 1
10 2
10 11
10 18
10 19
10 23
11 2
11 3
11 13
11 23
12 0
12 4
12 13
12 18
12 23
13 4
13 21
13 22
14 15
14 16
16 2
16 7
17 6
17 12
17 19
19 10
19 21
20 10
21 15
22 12
23 12
24 25
24 26
24 27
24 28
29 2
30 16

115 114
Shin-Hakodate-Hokuto
Kikonai
Yunosato-Shiriuchi
Yoshioka-Teiten
Tappi-Teiten
Oku-Tsugaru-Imabetsu
Shin-Nakaoguni
Shin-Aomori
Shichinohe-Towada
Hachinohe
Ninohe
Iwate-Numakunai
Morioka
Shin-Hanamaki
Kitakami
Mizusawa-Esashi
Ichinoseki
Kurikoma-Kogen
Furukawa
Sendai Eki
Shiroishi-Zao
Fukushima
Koriyama
Shin-Shirakawa
Nasushiobara
Utsunomiya
Oyama
Washinomiya
Omiya
Ueno
Tokyo
Shizukuishi
Tazawako
Kakunodate
Omagari
Akita
Yonezawa
Takahata
Akayu
Kaminoyama-Onsen
Yamagata
Tendo
Sakuranbo-Higashine
Murayama
Oishida
Shinjo
Kumagaya
Honjo-Waseda
Takasaki
Jomo-Kogen
Echigo-Yuzawa
Urasa
Nagaoka
Tsubame-Sanjo
Niigata
Annaka-Haruna
Karuizawa
Sakudaira
Ueda
Nagano
Iiyama
Joetsu-Myoko
Itoigawa
Kurobe-Unazuki-Onsen
Toyama
Shin-Takaoka
Kanazawa
Shinagawa
Shin-Yokohama
Odawara
Atami
Mishima
Shin-Fuji
Shizuoka
Kakegawa
Hamamatsu
Toyohashi
Mikawa-Anjo
Nagoya
Gifu-Hashima
Maibara
Ritto
Kyoto
Torikai
Shin-Osaka
Shin-Kobe
Nishi-Akashi
Himeji
Aioi
Okayama
Shin-Kurashiki
Fukuyama
Shin-Onomichi
Mihara
Higashi-Hiroshima
Hiroshima
Shin-Iwakuni
Tokuyama
Shin-Yamaguchi
Asa
Shin-Shimonoseki
Kokura
Kurate
Hakata
Shin-Tosu
Kurume
Chikugo-Funagoya
Shin-Omuta
Shin-Tamana
Kumamoto
Shin-Yatsushiro
Shin-Minamata
Izumi
Sendai
Kagoshima-Chuo
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
10 11
11 12
12 13
12 31
13 14
14 15
15 16
16 17
17 18
18 19
19 20
20 21
21 22
21 36
22 23
23 24
24 25
25 26
26 27
27 28
28 29
28 46
29 30
30 67
31 32
32 33
33 34
34 35
36 37
37 38
38 39
39 40
40 41
41 42
42 43
43 44
44 45
46 47
47 48
48 49
49 50
50 51
51 52
52 53
53 54
48 55
55 56
56 57
57 58
58 59
59 60
60 61
61 62
62 63
63 64
64 65
65 66
67 68
68 69
69 70
70 71
71 72
72 73
73 74
74 75
75 76
76 77
77 78
78 79
79 80
80 81
80 82
82 83
83 84
84 85
85 86
86 87
87 88
88 89
89 90
90 91
91 92
92 93
93 94
94 95
95 96
96 97
97 98
98 99
99 100
100 101
101 102
102 103
103 104
104 105
105 106
106 107
107 108
108 109
109 110
110 111
111 112
112 113
113 114

output
Far East is an articulation point. It separates the graph into 2 components.
East Coast of North America is an articulation point. It separates the graph into 2 components.
South-East Asia is an articulation point. It separates the graph into 3 components.
Europe is an articulation point. It separates the graph into 2 components.
Japan is an articulation point. It separates the graph into 5 components.

Kikonai is an articulation point. It separates the graph into 2 components.
Yunosato-Shiriuchi is an articulation point. It separates the graph into 2 components.
Yoshioka-Teiten is an articulation point. It separates the graph into 2 components.
Tappi-Teiten is an articulation point. It separates the graph into 2 components.
Oku-Tsugaru-Imabetsu is an articulation point. It separates the graph into 2 components.
Shin-Nakaoguni is an articulation point. It separates the graph into 2 components.
Shin-Aomori is an articulation point. It separates the graph into 2 components.
Shichinohe-Towada is an articulation point. It separates the graph into 2 components.
Hachinohe is an articulation point. It separates the graph into 2 components.
Ninohe is an articulation point. It separates the graph into 2 components.
Iwate-Numakunai is an articulation point. It separates the graph into 2 components.
Morioka is an articulation point. It separates the graph into 3 components.
Shin-Hanamaki is an articulation point. It separates the graph into 2 components.
Kitakami is an articulation point. It separates the graph into 2 components.
Mizusawa-Esashi is an articulation point. It separates the graph into 2 components.
Ichinoseki is an articulation point. It separates the graph into 2 components.
Kurikoma-Kogen is an articulation point. It separates the graph into 2 components.
Furukawa is an articulation point. It separates the graph into 2 components.
Sendai Eki is an articulation point. It separates the graph into 2 components.
Shiroishi-Zao is an articulation point. It separates the graph into 2 components.
Fukushima is an articulation point. It separates the graph into 3 components.
Koriyama is an articulation point. It separates the graph into 2 components.
Shin-Shirakawa is an articulation point. It separates the graph into 2 components.
Nasushiobara is an articulation point. It separates the graph into 2 components.
Utsunomiya is an articulation point. It separates the graph into 2 components.
Oyama is an articulation point. It separates the graph into 2 components.
Washinomiya is an articulation point. It separates the graph into 2 components.
Omiya is an articulation point. It separates the graph into 3 components.
Ueno is an articulation point. It separates the graph into 2 components.
Tokyo is an articulation point. It separates the graph into 2 components.
Shizukuishi is an articulation point. It separates the graph into 2 components.
Tazawako is an articulation point. It separates the graph into 2 components.
Kakunodate is an articulation point. It separates the graph into 2 components.
Omagari is an articulation point. It separates the graph into 2 components.
Yonezawa is an articulation point. It separates the graph into 2 components.
Takahata is an articulation point. It separates the graph into 2 components.
Akayu is an articulation point. It separates the graph into 2 components.
Kaminoyama-Onsen is an articulation point. It separates the graph into 2 components.
Yamagata is an articulation point. It separates the graph into 2 components.
Tendo is an articulation point. It separates the graph into 2 components.
Sakuranbo-Higashine is an articulation point. It separates the graph into 2 components.
Murayama is an articulation point. It separates the graph into 2 components.
Oishida is an articulation point. It separates the graph into 2 components.
Kumagaya is an articulation point. It separates the graph into 2 components.
Honjo-Waseda is an articulation point. It separates the graph into 2 components.
Takasaki is an articulation point. It separates the graph into 3 components.
Jomo-Kogen is an articulation point. It separates the graph into 2 components.
Echigo-Yuzawa is an articulation point. It separates the graph into 2 components.
Urasa is an articulation point. It separates the graph into 2 components.
Nagaoka is an articulation point. It separates the graph into 2 components.
Tsubame-Sanjo is an articulation point. It separates the graph into 2 components.
Annaka-Haruna is an articulation point. It separates the graph into 2 components.
Karuizawa is an articulation point. It separates the graph into 2 components.
Sakudaira is an articulation point. It separates the graph into 2 components.
Ueda is an articulation point. It separates the graph into 2 components.
Nagano is an articulation point. It separates the graph into 2 components.
Iiyama is an articulation point. It separates the graph into 2 components.
Joetsu-Myoko is an articulation point. It separates the graph into 2 components.
Itoigawa is an articulation point. It separates the graph into 2 components.
Kurobe-Unazuki-Onsen is an articulation point. It separates the graph into 2 components.
Toyama is an articulation point. It separates the graph into 2 components.
Shin-Takaoka is an articulation point. It separates the graph into 2 components.
Shinagawa is an articulation point. It separates the graph into 2 components.
Shin-Yokohama is an articulation point. It separates the graph into 2 components.
Odawara is an articulation point. It separates the graph into 2 components.
Atami is an articulation point. It separates the graph into 2 components.
Mishima is an articulation point. It separates the graph into 2 components.
Shin-Fuji is an articulation point. It separates the graph into 2 components.
Shizuoka is an articulation point. It separates the graph into 2 components.
Kakegawa is an articulation point. It separates the graph into 2 components.
Hamamatsu is an articulation point. It separates the graph into 2 components.
Toyohashi is an articulation point. It separates the graph into 2 components.
Mikawa-Anjo is an articulation point. It separates the graph into 2 components.
Nagoya is an articulation point. It separates the graph into 2 components.
Gifu-Hashima is an articulation point. It separates the graph into 2 components.
Maibara is an articulation point. It separates the graph into 3 components.
Kyoto is an articulation point. It separates the graph into 2 components.
Torikai is an articulation point. It separates the graph into 2 components.
Shin-Osaka is an articulation point. It separates the graph into 2 components.
Shin-Kobe is an articulation point. It separates the graph into 2 components.
Nishi-Akashi is an articulation point. It separates the graph into 2 components.
Himeji is an articulation point. It separates the graph into 2 components.
Aioi is an articulation point. It separates the graph into 2 components.
Okayama is an articulation point. It separates the graph into 2 components.
Shin-Kurashiki is an articulation point. It separates the graph into 2 components.
Fukuyama is an articulation point. It separates the graph into 2 components.
Shin-Onomichi is an articulation point. It separates the graph into 2 components.
Mihara is an articulation point. It separates the graph into 2 components.
Higashi-Hiroshima is an articulation point. It separates the graph into 2 components.
Hiroshima is an articulation point. It separates the graph into 2 components.
Shin-Iwakuni is an articulation point. It separates the graph into 2 components.
Tokuyama is an articulation point. It separates the graph into 2 components.
Shin-Yamaguchi is an articulation point. It separates the graph into 2 components.
Asa is an articulation point. It separates the graph into 2 components.
Shin-Shimonoseki is an articulation point. It separates the graph into 2 components.
Kokura is an articulation point. It separates the graph into 2 components.
Kurate is an articulation point. It separates the graph into 2 components.
Hakata is an articulation point. It separates the graph into 2 components.
Shin-Tosu is an articulation point. It separates the graph into 2 components.
Kurume is an articulation point. It separates the graph into 2 components.
Chikugo-Funagoya is an articulation point. It separates the graph into 2 components.
Shin-Omuta is an articulation point. It separates the graph into 2 components.
Shin-Tamana is an articulation point. It separates the graph into 2 components.
Kumamoto is an articulation point. It separates the graph into 2 components.
Shin-Yatsushiro is an articulation point. It separates the graph into 2 components.
Shin-Minamata is an articulation point. It separates the graph into 2 components.
Izumi is an articulation point. It separates the graph into 2 components.
Sendai is an articulation point. It separates the graph into 2 components.
*/
