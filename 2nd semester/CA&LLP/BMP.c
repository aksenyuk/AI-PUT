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


void hist(int arr[16], int sum){
    int lol = 0;
    for(int i = 0; i < 16; i++){
        printf("  %d-%d: %.2f%%\n", lol, lol+15, (double)(((double)arr[i]/(double)sum) * 100));
        lol += 16;
    }
}


int main (int argc, char *argv[])
{
    FILE *input_file;
    input_file = fopen(argv[1], "rb");
    BITMAPFILEHEADER *bmFileHeader = NULL;
    bmFileHeader = ReadBMFileHeader(input_file);
    printf("BITMAPFILEHEADER:\n  bfType:   0x%x\n  bfSize:   %d\n  bfReserved1:   0x%x\n  bfReserved2:   0x%x\n  bfOffBits:  %d\n",
           bmFileHeader->bfType, bmFileHeader->bfSize, bmFileHeader->bfReserved1, bmFileHeader->bfReserved2, bmFileHeader->bfOffBits);

    BITMAPINFOHEADER *bmInfoHeader = NULL;
    bmInfoHeader = ReadBMinfoHeader(input_file);
    printf("BITMAPINFOHEADER:\n  biSize:   %d\n  biWidth:   %d\n  biHeight:   %d\n  biPlanes:   %d\n  biBitCount:   %d\n"
           "biCompression:   %d\n  biSizeImage:   %d\n  biXPelsPerMeter: %d\n  biYPelsPerMeter: %d\n  biClrUsed:   %d\n  biClrImportant:  %d\n", bmInfoHeader->biSize, bmInfoHeader->biWidth, bmInfoHeader->biHeight, bmInfoHeader->biPlanes, bmInfoHeader->biBitCount, bmInfoHeader->biCompression, bmInfoHeader->biSizeImage, bmInfoHeader->biXPelsPerMeter, bmInfoHeader->biYPelsPerMeter, bmInfoHeader->biClrUsed, bmInfoHeader->biClrImportant);


    if(bmInfoHeader->biCompression != 0 || bmInfoHeader->biBitCount != 24){
        printf("Histogram calculation is unsupported");
        return 0;
    }


    int size=bmInfoHeader->biSizeImage/3, red[16] = {0}, green[16] = {0}, blue[16] = {0};

    unsigned char *wszystko;
    wszystko = (unsigned char*)malloc(bmInfoHeader->biSizeImage);
    fseek(input_file, 56, SEEK_SET);
    int counter = 0, width=bmInfoHeader->biWidth;
    while(width % 4 != 0) width--;

    for(int i = 0; i < bmInfoHeader->biHeight; i++)
        for(int j = 0; j < width*3; j++){
            fread(&wszystko[counter], 1, 1, input_file);
            counter++;
        }

    for(int i = 0; i < bmInfoHeader->biSizeImage; i+=3){
        blue[wszystko[i]/16] += 1;
        green[wszystko[i+1]/16] += 1;
        red[wszystko[i+2]/16] += 1;
    }

    printf("Red:\n"); hist(red, size);
    printf("Green:\n"); hist(green, size);
    printf("Blue:\n"); hist(blue, size);

    for(int i = 0; i < bmInfoHeader->biSizeImage; i+= 3){
        int j = (wszystko[i] + wszystko[i + 1] + wszystko[i + 2]) / 3;
        wszystko[i] = j;
        wszystko[i+1] = j;
        wszystko[i+2] = j;
    }

    fclose(input_file);

    FILE *grey;
    grey = fopen(argv[2], "wb");

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


    int counter2=0;
    for(int i = 0; i < bmInfoHeader->biHeight; i++){
        for(int j = 0; j < bmInfoHeader->biWidth*3; j++){
            fwrite(&wszystko[counter2], 1, 1, grey);
            counter2++;
        }

    }

    int padding = ((bmInfoHeader->biWidth * 3) / 4) - 4;
    for(int k = 0; k < padding; k++){
    	fputc(0x00, grey);
    	fputc(0x00, grey);
    	fputc(0x00, grey);
    }

    free(wszystko);
    fclose(grey);

    return 0;
}
;
