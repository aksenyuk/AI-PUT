#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef uint16_t WORD;
typedef uint32_t DWORD;
typedef int32_t LONG;

typedef struct tagBITMAPFILEHEADER {
  WORD  bfType;
  DWORD bfSize;
  WORD  bfReserved1;
  WORD  bfReserved2;
  DWORD bfOffBits;
} BITMAPFILEHEADER, *LPBITMAPFILEHEADER, *PBITMAPFILEHEADER;

typedef struct tagBITMAPINFOHEADER {
  DWORD biSize;
  LONG  biWidth;
  LONG  biHeight;
  WORD  biPlanes;
  WORD  biBitCount;
  DWORD biCompression;
  DWORD biSizeImage;
  LONG  biXPelsPerMeter;
  LONG  biYPelsPerMeter;
  DWORD biClrUsed;
  DWORD biClrImportant;
} BITMAPINFOHEADER, *LPBITMAPINFOHEADER, *PBITMAPINFOHEADER;



BITMAPFILEHEADER *ReadBMFileHeader(FILE *fp)
{
    BITMAPFILEHEADER *header = (BITMAPFILEHEADER *)malloc(sizeof(BITMAPFILEHEADER));
    fread(&header->bfType, 2, 1, fp);
    fread(&header->bfSize, 4, 1, fp);
    fread(&header->bfReserved1, 2, 1, fp);
    fread(&header->bfReserved2, 2, 1, fp);
    fread(&header->bfOffBits, 4, 1, fp);
    return header;
}

BITMAPINFOHEADER *ReadBMinfoHeader(FILE *fp)
{
    BITMAPINFOHEADER *header2 = (BITMAPINFOHEADER *)malloc(sizeof(BITMAPINFOHEADER));
    fread(&header2->biSize, 4, 1, fp);
    fread(&header2->biWidth, 4, 1, fp);
    fread(&header2->biHeight, 4, 1, fp);
    fread(&header2->biPlanes, 2, 1, fp);
    fread(&header2->biBitCount, 2, 1, fp);
    fread(&header2->biCompression, 4, 1, fp);
    fread(&header2->biSizeImage, 4, 1, fp);
    fread(&header2->biXPelsPerMeter, 4, 1, fp);
    fread(&header2->biYPelsPerMeter, 4, 1, fp);
    fread(&header2->biClrUsed, 4, 1, fp);
    fread(&header2->biClrImportant, 4, 1, fp);
    return header2;
}


void persent(int arr[16], int sum){
    int lol = 0;
    for(int i = 0; i < 16; i++){
        printf("  %d-%d: %.2f%%\n", lol, lol+15, (double)(((double)arr[i]/(double)sum) * 100));
        lol += 16;
    }
}




int main (int argc, char *argv[])
{
    FILE *input_file;
    input_file = fopen("C:/Users/Vladimir/STUDY/Semester 2/CALLP/rep2/c-programming.bmp", "rb");
    BITMAPFILEHEADER *bmFileHeader = NULL;
    bmFileHeader = ReadBMFileHeader(input_file);
    printf("BITMAPFILEHEADER:\n  bfType:\t%10   0x%x\n  bfSize:\t%10   %d\n  bfReserved1:\t%10   0x%x\n  bfReserved2:\t%10   0x%x\n  bfOffBits:\t%10   %d\n",
           bmFileHeader->bfType, bmFileHeader->bfSize, bmFileHeader->bfReserved1, bmFileHeader->bfReserved2, bmFileHeader->bfOffBits);

    BITMAPINFOHEADER *bmInfoHeader = NULL;
    bmInfoHeader = ReadBMinfoHeader(input_file);
    printf("BITMAPINFOHEADER:\n  biSize:\t%12   %d\n  biWidth:\t%12   %d\n  biHeight:\t%12   %d\n  biPlanes:\t%12   %d\n  biBitCount:\t%12   %d\n"
           "biCompression:   %d\n  biSizeImage:\t%12   %d\n  biXPelsPerMeter: %d\n  biYPelsPerMeter: %d\n  biClrUsed:\t%12   %d\n  biClrImportant:  %d\n", bmInfoHeader->biSize, bmInfoHeader->biWidth, bmInfoHeader->biHeight, bmInfoHeader->biPlanes, bmInfoHeader->biBitCount, bmInfoHeader->biCompression, bmInfoHeader->biSizeImage, bmInfoHeader->biXPelsPerMeter, bmInfoHeader->biYPelsPerMeter, bmInfoHeader->biClrUsed, bmInfoHeader->biClrImportant);




    if(bmInfoHeader->biCompression != 0 || bmInfoHeader->biBitCount != 24){
        printf("Histogram calculation is unsupported");
        return 0;
    }


    int red[16] = {0}, green[16] = {0}, blue[16] = {0};

    unsigned char *bitmapImage;
    bitmapImage = (unsigned char*)malloc(bmInfoHeader->biSizeImage);
    fread(bitmapImage,bmInfoHeader->biSizeImage,1,input_file);

    for (int imageIdx = 0;imageIdx < bmInfoHeader->biSizeImage;imageIdx+=3)
    {
        int tempRGB = bitmapImage[imageIdx];
        bitmapImage[imageIdx] = bitmapImage[imageIdx + 2];
        bitmapImage[imageIdx + 2] = tempRGB;
    }

    for(int i = 0; i < bmInfoHeader->biSizeImage; i+=3){
        red[bitmapImage[i]/16] += 1;
        green[bitmapImage[i+1]/16] += 1;
        blue[bitmapImage[i+2]/16] += 1;
    }

    int sum1=0, sum2=0, sum3=0;
    for(int i=0; i < 16; i++){
        sum1 += red[i];
        sum2 += green[i];
        sum3 += blue[i];
    }

    printf("Red:\n"); persent(red, sum1);
    printf("Green:\n"); persent(green, sum2);
    printf("Blue:\n"); persent(blue, sum3);




    for(int i = 0; i < bmInfoHeader->biSizeImage; i+= 3){
        int j = (bitmapImage[i] + bitmapImage[i + 1] + bitmapImage[i + 2]) / 3;
        bitmapImage[i] = j;
        bitmapImage[i+1] = j;
        bitmapImage[i+2] = j;
    }

    fclose(input_file);


    FILE *grey;
    grey = fopen("C:/Users/Vladimir/STUDY/Semester 2/CALLP/rep2/greyyy.bmp", "wb");

    fwrite(&bmFileHeader->bfType, 2, 1, grey);
    fwrite(&bmFileHeader->bfSize, 4, 1, grey);
    fwrite(&bmFileHeader->bfReserved1, 2, 1, grey);
    fwrite(&bmFileHeader->bfReserved2, 2, 1, grey);
    fwrite(&bmFileHeader->bfOffBits, 4, 1, grey);

    fwrite(&bmInfoHeader->biSize, 4, 1, grey);
    fwrite(&bmInfoHeader->biWidth, 4, 1, grey);
    fwrite(&bmInfoHeader->biHeight, 4, 1, grey);
    fwrite(&bmInfoHeader->biPlanes, 2, 1, grey);
    fwrite(&bmInfoHeader->biBitCount, 2, 1, grey);
    fwrite(&bmInfoHeader->biCompression, 4, 1, grey);
    fwrite(&bmInfoHeader->biSizeImage, 4, 1, grey);
    fwrite(&bmInfoHeader->biXPelsPerMeter, 4, 1, grey);
    fwrite(&bmInfoHeader->biYPelsPerMeter, 4, 1, grey);
    fwrite(&bmInfoHeader->biClrUsed, 4, 1, grey);
    fwrite(&bmInfoHeader->biClrImportant, 4, 1, grey);

    //fwrite(bitmapImage, 1, bmInfoHeader->biSizeImage, grey);

    int padding = ((bmInfoHeader->biWidth * 3) / 4) - 4;

    for (int i = 0; i < bmInfoHeader->biSizeImage; i++) {
        //for(int j = 0; j < bmInfoHeader->biWidth; j++)
        fwrite(&bitmapImage[i], 1, 1, grey);
        //if (i % bmInfoHeader->biWidth == 0 && i > bmInfoHeader->biWidth){
            //fputc(0x00, grey);
        }
    for(int i = 0; i < padding; i++)
        fputc(0x00, grey);

        //fwrite((unsigned char)0x00, 1, 1, grey);
        //fwrite((unsigned char)0x00, 1, 1, grey);
       // fwrite((unsigned char)0x00, 1, 1, grey);

    //printf("%d ", padding);

    //for(int i = 0; i < padding; i++)
        //fputc((unsigned char)0xFF, grey);

    fclose(grey);

    return 0;
}
