#include <stdio.h>

void writeCSVfiles() {
    FILE *employees_data;
    FILE *coords_data;
    FILE *missions_data;
    
    employees_data = fopen("./csv/employees_data.csv", "w+");
    coords_data = fopen("./csv/coords_data.csv", "w+");
    missions_data = fopen("./csv/missions_data.csv", "w+");

    fprintf(employees_data, "Signes, LPC, Menuiserie, Electricité, Mécanique, Informatique, Cuisine\n");
    for (int i = 0; i < NBR_INTERFACES; i++) {
        fprintf(employees_data, "%d, %d, %d, %d, %d, %d, %d\n", competences_interfaces[i][0], competences_interfaces[i][1], 
            specialite_interfaces[i][0], specialite_interfaces[i][1], specialite_interfaces[i][2], specialite_interfaces[i][3]
            , specialite_interfaces[i][4]);
    }

    fprintf(coords_data, "Centre SESSAD, %d, %d\n", coord[0][0], coord[0][1]);
    fprintf(coords_data, "Centre Formation Menuiserie, %d, %d\n", coord[1][0], coord[1][1]);
    fprintf(coords_data, "Centre Formation Electricité, %d, %d\n", coord[2][0], coord[2][1]);
    fprintf(coords_data, "Centre Formation Mécanique, %d, %d\n", coord[3][0], coord[3][1]);
    fprintf(coords_data, "Centre Formation Informatique, %d, %d\n", coord[4][0], coord[4][1]);
    fprintf(coords_data, "Centre Formation Cuisine, %d, %d\n", coord[5][0], coord[5][1]);

    fprintf(missions_data, "ID, Specialité (Menuiserie-Cuisine = 0-4), Compétence (Codage/LPC = 0/1), Jour (Lun-Sam = 1-6), Horaire Début (h), Horaire Fin (h), Coordonnées X, Coordonnées Y\n");
    for (int i = 0; i < NBR_FORMATION; i++) {
        fprintf(missions_data, "%d, %d, %d, %d, %d, %d, %d, %d\n", formation[i][0], formation[i][1], formation[i][2], formation[i][3],
            formation[i][4], formation[i][5], coord[i + 6][0], coord[i + 6][1]);
    }
}