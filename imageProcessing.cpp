/*
Image processing: ppm image
Read file, write file, struct
Author: 10831415
Date: 2021/01/10
*/

#include<iostream>
#include<fstream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<ctime>
using namespace std;

#define HIGHT 5000      //Max length
#define WIDTH 5000      //Max width
#define MAXN 5000

struct Pixel{
    int R, G, B;
};

struct Image{
  Pixel val[MAXN][MAXN];
  int row, col; //image size
  string type; //image type p3,p5,p6
  int mode; //image color model 255 means 0-255, 256 colors
};

///(PROTOTYPE)
void openFile();
void readImage(Image& image);
void writeImage(const Image& image);
void closeFile();
void copy(const Image& image1, Image& image2);
void shrink(const Image& image1, Image& image2) ;
void enlarge(const Image& image1, Image& image2) ;
void rotate(const Image& image1, Image& image2) ;
void vMirror(const Image& image1, Image& image2) ;
void hMirror(const Image& image1, Image& image2) ;
void grayScale(int l, const Image& image1, Image& image2) ;
void singleColorScale(int color, const Image& image1, Image& image2) ;
void removeSingleColor(int color, const Image& image1, Image& image2) ;
void pixelMosaic(int level1, const Image& image1, Image& image2) ;
void negative(const Image& image1, Image& image2) ;
void overlay(const Image& image1, const Image& image2, Image& image3) ;
void colorMosaic(const Image& image1, Image& image2) ;
void exchangeColor(int choice, const Image& image1, Image& image2) ;
void sharpFilter(const Image& image1, Image& image2) ;
void cut(const Image& image1, const Image& image2, Image& image3) ;
void gradual(int c, const Image& image1, Image& image2) ;

///variations

fstream fin;
fstream fout;
Image image1 ;
Image image2 ;
Image image3 ;

/// main function
int main(){
  while(true){
    cout << "What function do you want to do?" << endl
      << "(1)Copy (2)Shrink (3)Enlarge (4)Rotate (5)Vertical Mirror"
      << endl <<"(6)Horizontal Mirror (7)Gray Scale (8)Red Scale "
      << "(9)Green Scale (10)Blue Scale" << endl << "(11)Remove Red "
      << "(12)Remove Green (13)Remove Blue (14)Pixel Mosaic "
      << "(15)Negative " << endl << "(16)Color Mosaic "
      << "(17)Exchange Colors (18)Sharpen (19)Gradual (20)Overlay" << endl ;

    int n_function ;
    cin >> n_function ;

    if(n_function<20){
      openFile();
      readImage(image1);
      switch(n_function){
        case 1:
          copy(image1, image2) ;
          break ;
        case 2:
          shrink(image1, image2) ;
          break ;
        case 3:
          enlarge(image1, image2) ;
          break ;
        case 4:
          rotate(image1, image2) ;
          break ;
        case 5:
          vMirror(image1, image2) ;
          break ;
        case 6:
          hMirror(image1, image2) ;
          break ;
        case 7:
          int l ;
          cout << "Which one do you want?" << endl
            << "(1)The common one (2)The Adobe Photoshop one" << endl
            << "Please enter your choice: " ;
          cin>>l ;
          grayScale(l, image1, image2) ;
          break ;
        case 8:
          singleColorScale(0, image1, image2) ;
          break ;
        case 9:
          singleColorScale(1, image1, image2) ;
          break ;
        case 10:
          singleColorScale(2, image1, image2) ;
          break ;
        case 11:
          removeSingleColor(0, image1, image2) ;
          break ;
        case 12:
          removeSingleColor(1, image1, image2) ;
          break ;
        case 13:
          removeSingleColor(2, image1, image2) ;
          break ;
        case 14:
          int level1 ;
          cout << "How blurry do you want?" << endl
            << "(1)A little (2)So so (3) Very" << endl
            << "Please enter your choice: " ;
          cin>>level1 ;
          pixelMosaic(level1, image1, image2) ;
          break ;
        case 15:
          negative(image1, image2) ;
          break ;
        case 16:
          colorMosaic(image1, image2) ;
          break ;
        case 17:
          int choice ;
          cout << "What kind of color exchange do you want?" << endl
            << "(1)RBG (2)BRG (3)BGR (4)GRB (5)GBR" << endl
            << "Please enter your choice: " ;
          cin>>choice ;
          exchangeColor(choice, image1, image2) ;
          break ;
        case 18:
          sharpFilter(image1, image2) ;
          break ;
        case 19:
          cout << "What color of gradual do you want?" << endl ;
          cout << "(1)Red (2)Green (3)Blue (4)Yellow (5)Cyan (6)Magenta "
            << "(7)Gray" << endl << "Please enter your choice: " ;
          int c ;
          cin >> c ;
          cout << endl ;
          gradual(c, image1, image2) ;
        default:
          break ;
      }
      writeImage(image2);
      closeFile();
    } else{
      openFile();
      readImage(image1);
      closeFile() ;
      openFile();
      readImage(image2);
      overlay(image1, image2, image3) ;
      //cut(image1, image2, image3) ;
      writeImage(image3);
      closeFile();
    }
  }
  return 0;
}


///function

void openFile(){
    char infile[20];
    cout << "Input your filename (ex: corner.ppm, lenna.ppm... ):";
    cin >> infile;
    fin.open(infile, ios::in); //open input file   ex: original.ppm, lena.ppm,.....

    if(!fin) cout << "Fail to open file: " << endl;
}

void readImage(Image& image){
  fin >> image.type;
  fin >> image.col >> image.row;
  fin >> image.mode;
  for (int i=0; i<image.row; i++){
    for (int j=0; j<image.col; j++){
      Pixel& p = image.val[i][j] ;
      fin >> p.R >> p.G >> p.B ;
    }
  }
      //fin >> image1[i][j].R >> image1[i][j].G >> image1[i][j].B ;
  cout << "Image size:" << image.col << " x "  << image.row << endl;
  cout << "Read Image Successfully!" << endl;
  //return a;
}

void copy(const Image& image1, Image& image2){
  image2.mode=image1.mode ;
  image2.type = image1.type ;
  image2.row=image1.row ;
  image2.col = image1.col ;
  for(int i=0 ; i<image1.row ; i++){
    for(int j=0 ; j<image1.col ; j++){
      image2.val[i][j] = image1.val[i][j] ;
    }
  }
}

void shrink(const Image& image1, Image& image2){
  image2.mode=image1.mode ;
  image2.type = image1.type ;
  image2.row=image1.row/2 ;
  image2.col = image1.col/2 ;
  for(int i1=0, i2=0 ; i1<image1.row ; i1+=2, i2++){
    for(int j1=0, j2=0 ; j1<image1.col ; j1+=2, j2++){
      image2.val[i2][j2] = image1.val[i1][j1] ;
    }
  }
}

void enlarge(const Image& image1, Image& image2){
  image2.mode=image1.mode ;
  image2.type = image1.type ;
  image2.row=image1.row*2 ;
  image2.col = image1.col*2 ;
  for(int i1=0, i2=0 ; i1<image1.row ; i1++, i2+=2){
    for(int j1=0, j2=0 ; j1<image1.col ; j1++, j2+=2){
      image2.val[i2][j2] = image2.val[i2][j2+1] = image2.val[i2+1][j2] =
        image2.val[i2+1][j2+1] = image1.val[i1][j1] ;
    }
  }
}

void hMirror(const Image& image1, Image& image2){
  image2.mode=image1.mode ;
  image2.type = image1.type ;
  image2.row=image1.row ;
  image2.col = image1.col ;
  for (int i1=image1.row-1, i2=0 ; i1>=0 ; i1--, i2++){
    for (int j=0 ; j<image1.col ; j++){
      image2.val[i2][j] = image1.val[i1][j] ;
    }
  }
}

void vMirror(const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;
  for(int r=0 ; r<image1.row ; r++){
    for(int c2=0, c1=image1.col-1 ; c2<image2.col ; c2++, c1--){
      image2.val[r][c2] = image1.val[r][c1];
    }
  }
}

void rotate(const Image& image1, Image& image2){
  image2.mode=image1.mode ;
  image2.type = image1.type ;
  image2.row=image1.col ;
  image2.col = image1.row ;
  for(int r2=0, c1=0 ; r2<image2.row ; r2++, c1++){
    for(int c2=0, r1=image1.row-1 ; c2<image2.col ; c2++, r1--){
      image2.val[r2][c2] = image1.val[r1][c1];
    }
  }
}

void grayScale(int l, const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;

  for(int r=0 ; r<image1.row ; r++){
    for(int c=0 ; c<image1.col ; c++){
      const Pixel& p=image1.val[r][c] ;
      int gray ;
      if(l==1) gray = 0.299*p.R + 0.587*p.G + 0.114*p.B ;
      else gray=pow((pow(p.R, 2.2)*0.2973+pow(p.G, 2.2)*0.6274+pow(p.B, 2.2)*0.0753), (1/2.2)) ;
      image2.val[r][c] = {gray, gray, gray} ;
    }
  }
}

void singleColorScale(int color, const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;

  switch(color){
    case 0:
      for(int r=0 ; r<image1.row ; r++){
        for(int c=0 ; c<image1.col ; c++){
          image2.val[r][c] = {image1.val[r][c].R, 0, 0} ;
        }
      }
      break ;
    case 1:
      for(int r=0 ; r<image1.row ; r++){
        for(int c=0 ; c<image1.col ; c++){
          image2.val[r][c] = {0, image1.val[r][c].G, 0} ;
        }
      }
      break ;
    case 2:
      for(int r=0 ; r<image1.row ; r++){
        for(int c=0 ; c<image1.col ; c++){
          image2.val[r][c] = {0, 0, image1.val[r][c].B} ;
        }
      }
      break ;
  }
}

void removeSingleColor(int color, const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;

  switch(color){
    case 0:
      for(int r=0 ; r<image1.row ; r++){
        for(int c=0 ; c<image1.col ; c++){
          const Pixel& p = image1.val[r][c] ;
          image2.val[r][c] = {0, p.G, p.B} ;
        }
      }
      break ;
    case 1:
      for(int r=0 ; r<image1.row ; r++){
        for(int c=0 ; c<image1.col ; c++){
          const Pixel& p = image1.val[r][c] ;
          image2.val[r][c] = {p.R, 0, p.B} ;
        }
      }
      break ;
    case 2:
      for(int r=0 ; r<image1.row ; r++){
        for(int c=0 ; c<image1.col ; c++){
          const Pixel& p = image1.val[r][c] ;
          image2.val[r][c] = {p.R, p.G, 0} ;
        }
      }
      break ;
  }
}

constexpr int KERNEL_WEIGHT1=965 ;

int kernel1[11][11]={
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 13, 22, 13, 0, 0, 0, 0},
  {0, 0, 0, 13, 59, 97, 59, 13, 0, 0, 0},
  {0, 0, 0, 22, 97, 149, 97, 22, 0, 0, 0},
  {0, 0, 0, 13, 59, 97, 59, 13, 0, 0, 0},
  {0, 0, 0, 0, 13, 22, 13, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
} ;

constexpr double KERNEL_WEIGHT2=992 ;

int kernel2[11][11]={
  {0, 2, 3, 4, 5, 5, 5, 4, 3, 2, 0},
  {2, 3, 5, 7, 8, 8, 8, 7, 5, 3, 2},
  {3, 5, 7, 10, 12, 12, 12, 10, 7, 5, 3},
  {4, 7, 10, 13, 15, 16, 15, 13, 10, 7, 4},
  {5, 8, 12, 15, 18, 19, 18, 15, 12, 8, 5},
  {5, 8, 12, 16, 19, 20, 19, 16, 12, 8, 5},
  {5, 8, 12, 15, 18, 19, 18, 15, 12, 8, 5},
  {4, 7, 10, 13, 15, 16, 15, 13, 10, 7, 4},
  {3, 5, 7, 10, 12, 12, 12, 10, 7, 5, 3},
  {2, 3, 5, 7, 8, 8, 8, 7, 5, 3, 2},
  {0, 2, 3, 4, 5, 5, 5, 4, 3, 2, 0}
} ;

constexpr int KERNEL_WEIGHT3=980 ;

int kernel3[11][11]={
  {0, 5, 6, 7, 7, 7, 7, 7, 6, 5, 0},
  {5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5},
  {6, 7, 8, 9, 10, 10, 10, 9, 8, 7, 6},
  {7, 8, 9, 10, 11, 11, 11, 10, 9, 8, 7},
  {7, 9, 10, 11, 11, 12, 11, 11, 10, 9, 7},
  {7, 9, 10, 11, 12, 12, 12, 11, 10, 9, 7},
  {7, 9, 10, 11, 11, 12, 11, 11, 10, 9, 7},
  {7, 8, 9, 10, 11, 11, 11, 10, 9, 8, 7},
  {6, 7, 8, 9, 10, 10, 10, 9, 8, 7, 6},
  {5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5},
  {0, 5, 6, 7, 7, 7, 7, 7, 6, 5, 0}
} ;

Pixel singleMosaicPixel(int level, Pixel& p, const Image& image, int r, int c){
  int R, G, B ;
  R=G=B=0 ;

  switch(level){
    case 1:
      for(int i=0 ; i<11 ; i++){
        for(int j=0 ; j<11 ; j++){
          const Pixel& tmp = image.val[r+i-1][c+j-1] ;
          //if(r+i-1<0 || r+i-1>=r || c+j-1<0 || c+j-1>=c) continue ;
          R+=kernel1[i][j]*tmp.R ;
          G+=kernel1[i][j]*tmp.G ;
          B+=kernel1[i][j]*tmp.B ;
        }
      }
      R=round(R/KERNEL_WEIGHT1) ;
      G=round(G/KERNEL_WEIGHT1) ;
      B=round(B/KERNEL_WEIGHT1) ;
      break ;
    case 2:
      for(int i=0 ; i<11 ; i++){
        for(int j=0 ; j<11 ; j++){
          const Pixel& tmp = image.val[r+i-1][c+j-1] ;
          //if(r+i-1<0 || r+i-1>=r || c+j-1<0 || c+j-1>=c) continue ;
          R+=kernel2[i][j]*tmp.R ;
          G+=kernel2[i][j]*tmp.G ;
          B+=kernel2[i][j]*tmp.B ;
        }
      }
      R=round(R/KERNEL_WEIGHT2) ;
      G=round(G/KERNEL_WEIGHT2) ;
      B=round(B/KERNEL_WEIGHT2) ;
      break ;
    case 3:
      for(int i=0 ; i<11 ; i++){
        for(int j=0 ; j<11 ; j++){
          const Pixel& tmp = image.val[r+i-1][c+j-1] ;
          //if(r+i-1<0 || r+i-1>=r || c+j-1<0 || c+j-1>=c) continue ;
          R+=kernel3[i][j]*tmp.R ;
          G+=kernel3[i][j]*tmp.G ;
          B+=kernel3[i][j]*tmp.B ;
        }
      }
      R=round(R/KERNEL_WEIGHT3) ;
      G=round(G/KERNEL_WEIGHT3) ;
      B=round(B/KERNEL_WEIGHT3) ;
      break ;
    default:
      break ;
  }
  return p={R, G, B} ;
}

void pixelMosaic(int level, const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;

  for(int r=0 ; r<image1.row ; r++){
    for(int c=0 ; c<image1.col ; c++){
      image2.val[r][c] = image1.val[r][c] ;
    }
  }

  for (int r=0 ; r<image1.row ; r++){
    for (int c=0 ; c<image1.col ; c++){
      image2.val[r][c] = singleMosaicPixel(level, image2.val[r][c], image1, r, c) ;
    }
  }
}

void negative(const Image& image1, Image& image2){
  image2.mode=image1.mode ;
  image2.type = image1.type ;
  image2.row=image1.row ;
  image2.col = image1.col ;
  for(int r=0 ; r<image1.row ; r++){
    for(int c=0 ; c<image1.col ; c++){
      const Pixel& p1=image1.val[r][c] ;
      image2.val[r][c] = {255-p1.R, 255-p1.G, 255-p1.B} ;
    }
  }
}

void colorMosaic(const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;
  for (int r=1 ; r<image1.row-1 ; r++){
    for (int c=1 ; c<image1.col-1 ; c++){
      const Pixel& p=image1.val[r][c] ;
      int R=round(p.R/20*5) ;
      int G=round(p.G/20*5) ;
      int B=round(p.B/20*5) ;
      image2.val[r][c]={R, G, B} ;
    }
  }
}

void exchangeColor(int choice, const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;

  switch(choice){
    case 1:
      for (int r=0 ; r<image1.row ; r++){
        for (int c=0 ; c<image1.col ; c++){
          const Pixel& p=image1.val[r][c] ;
          image2.val[r][c]={p.R, p.B, p.G} ;
        }
      }
      break ;
    case 2:
      for (int r=0 ; r<image1.row ; r++){
        for (int c=0 ; c<image1.col ; c++){
          const Pixel& p=image1.val[r][c] ;
          image2.val[r][c]={p.B, p.R, p.G} ;
        }
      }
      break ;
    case 3:
      for (int r=0 ; r<image1.row ; r++){
        for (int c=0 ; c<image1.col ; c++){
          const Pixel& p=image1.val[r][c] ;
          image2.val[r][c]={p.B, p.G, p.R} ;
        }
      }
      break ;
    case 4:
      for (int r=0 ; r<image1.row ; r++){
        for (int c=0 ; c<image1.col ; c++){
          const Pixel& p=image1.val[r][c] ;
          image2.val[r][c]={p.G, p.R, p.B} ;
        }
      }
      break ;
    case 5:
      for (int r=0 ; r<image1.row ; r++){
        for (int c=0 ; c<image1.col ; c++){
          const Pixel& p=image1.val[r][c] ;
          image2.val[r][c]={p.G, p.B, p.R} ;
        }
      }
      break ;
    default:
      break ;
  }
}

constexpr int S_KERNEL_WEIGHT=997 ;

int s_kernel[11][11]={
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, -1, -2, -1, 0, 0, 0, 0},
  {0, 0, 0, -3, -13, -22, -13, -3, 0, 0, 0},
  {0, 0, -1, -13, -59, -97, -59, -13, -1, 0, 0},
  {0, 0, -2, -22, -97, 1841, -97, -22, -2, 0, 0},
  {0, 0, -1, -13, -59, -97, -59, -13, -1, 0, 0},
  {0, 0, 0, -3, -13, -22, -13, -3, 0, 0, 0},
  {0, 0, 0, 0, -1, -2, -1, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
} ;

Pixel singlePixelSharp(Pixel& p, const Image& image, int r, int c){
  int R, G, B ;
  R=G=B=0 ;

    for(int i=0 ; i<11 ; i++){
      for(int j=0 ; j<11 ; j++){
        const Pixel& tmp = image.val[r+i-1][c+j-1] ;
        //if(r+i-1<0 || r+i-1>=r || c+j-1<0 || c+j-1>=c) continue ;
        R+=s_kernel[i][j]*tmp.R ;
        G+=s_kernel[i][j]*tmp.G ;
        B+=s_kernel[i][j]*tmp.B ;
      }
    }
    R=round(R/S_KERNEL_WEIGHT) ;
    G=round(G/S_KERNEL_WEIGHT) ;
    B=round(B/S_KERNEL_WEIGHT) ;
  return p={R, G, B} ;
}

void sharpFilter(const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;

  for(int r=0 ; r<image1.row ; r++){
    for(int c=0 ; c<image1.col ; c++){
      image2.val[r][c] = image1.val[r][c] ;
    }
  }

  for (int r=0 ; r<image1.row ; r++){
    for (int c=0 ; c<image1.col ; c++){
      Pixel p1=singleMosaicPixel(1, image2.val[r][c], image1, r, c) ;
      Pixel p2=singlePixelSharp(image2.val[r][c], image1, r, c) ;
      int R=p1.R+p2.R, G=p1.G+p2.G, B=p1.B+p2.B ;
      if(R<0) R=0 ;
      if(G<0) G=0 ;
      if(B<0) B=0 ;
      if(R>255) R=255 ;
      if(G>255) G=255 ;
      if(B>255) B=255 ;
      image2.val[r][c]={R, G, B} ;
    }
  }
}

void gradual(int c, const Image& image1, Image& image2){
  image2.mode = image1.mode ;
  image2.type = image1.type ;
  image2.row = image1.row ;
  image2.col = image1.col ;

  switch(c){
    case 1:
      const int rc_sum = image1.row+image1.col ;
      for(int r=0 ; r<image1.row ; r++){
        for(int c=0 ; c<image1.col ; c++){
          const double rc_per = 1.0*(r+c)/rc_sum ;
          image2.val[r][c] = image1.val[r][c] ;
          image2.val[r][c].R*=rc_per ;
        }
      }
      break ;
  }
  /*
  const int rc_sum = image1.row+image1.col ;
  for(int r=0 ; r<image1.row ; r++){
    for(int c=0 ; c<image1.col ; c++){
      const double r_per=1.0*(r+c)/rc_sum ;
      image2.val[r][c] = image1.val[r][c] ;
      image2.val[r][c].R*=r_per ;
      image2.val[r][c].G*=r_per ;
      image2.val[r][c].B*=r_per ;
    }
  }
  */
}

void overlay(const Image& image1, const Image& image2, Image& image3){
  image3.mode=image1.mode ;
  image3.type = image1.type ;
  image3.row=image1.row ;
  image3.col = image1.col ;
  for(int r=0 ; r<image1.row ; r++){
    for(int c=0 ; c<image1.col ; c++){
      const Pixel& p1=image1.val[r][c] ;
      const Pixel& p2=image2.val[r][c] ;
      int R=p1.R*0.8+p2.R*0.2 ;
      int G=p1.G*0.8+p2.G*0.2 ;
      int B=p1.B*0.8+p2.B*0.2 ;

      image3.val[r][c] = {R, G, B} ;
    }
  }
}

/*
void cut(const Image& image1, const Image& image2, Image& image3){
  image3.mode=image1.mode ;
  image3.type = image1.type ;
  image3.row=image1.row ;
  image3.col = image1.col ;

  for(int r=0 ; r<image1.row ; r++){
    for(int c=0 ; c<image1.col ; c++){
      const Pixel& p=image1.val[r][c] ;
      //if(p.R+p.G+p.B >= 750) image3.val[r][c]={255, 255, 255} ;
      //else image3.val[r][c] = image2.val[r][c] ;
      if(p.R+p.G+p.B <= 300) image3.val[r][c]=p;
      else image3.val[r][c] = image2.val[r][c] ;
    }
  }
}
*/

void writeImage(const Image& image){
    char outfile[20];
    cout << "Input your  Output filename (ex: corner_copy.ppm, lenna_copy.ppm... ):";
    cin >> outfile;             // ex: corner_copy.ppm, lenna_copy.ppm

    fout.open(outfile, ios::out); //open output file
    fout << image.type << endl;
    fout << image.col << " " << image.row << endl;
    fout << image.mode << endl;

    for (int i=0; i<image.row; i++){
        for (int j=0; j<image.col; j++){
          const Pixel& p=image.val[i][j] ;
          fout << p.R << " " << p.G << " " << p.B << " ";
        }
        fout << endl;
    }

    cout << "Write Image Successfully!!"  << endl << endl ;
    fout.close(); //close output file
}

void closeFile(){
    fin.close();  //close input file
}
