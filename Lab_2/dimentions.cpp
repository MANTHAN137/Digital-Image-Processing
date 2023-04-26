#include <stdio.h>

int main() {
    FILE *fp = fopen("image.bmp", "rb"); // replace with your image file name
    unsigned char header[54]; // BMP header is 54 bytes long
    int width, height;

    // read the BMP header to get the width and height
    fread(header, sizeof(unsigned char), 54, fp);
    width = *(int*)&header[18];
    height = *(int*)&header[22];

    printf("Image dimensions: %d x %d\n", width, height);

    fclose(fp);
    return 0;
}





