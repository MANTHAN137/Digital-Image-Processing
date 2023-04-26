#include <stdio.h>
#include <stdlib.h>

int main() {
    // Open the input file for reading
    FILE *input_file = fopen("image.png", "rb");
    if (input_file == NULL) {
        printf("Error opening input file\n");
        return 1;
    }

    // Read the contents of the input file
    fseek(input_file, 0, SEEK_END);
    long input_file_size = ftell(input_file);
    rewind(input_file);

    char *input_file_contents = (char*)malloc(input_file_size * sizeof(char));
    if (input_file_contents == NULL) {
        printf("Error allocating memory\n");
        fclose(input_file);
        return 1;
    }

    fread(input_file_contents, sizeof(char), input_file_size, input_file);

    // Close the input file
    fclose(input_file);
    

    // Open the output file for writing
    FILE *output_file = fopen("EditedImage.png", "wb");
    if (output_file == NULL) {
        printf("Error opening output file\n");
        free(input_file_contents);
        return 1;
    }

    // Write the contents of the input file to the output file
    fwrite(input_file_contents, sizeof(char), input_file_size, output_file);

    // Close the output file
    fclose(output_file);

    // Free the memory used to store the contents of the input file
    free(input_file_contents);

    return 0;
}
