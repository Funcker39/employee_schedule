#include <stdio.h>
                  
#define NBR_INTERFACES        24
#define NBR_APPRENANTS        80
#define NBR_FORMATIONS        80
#define NBR_CENTRES_FORMATION 5
#define NBR_SPECIALITES       5
#define NBR_NODES 	      NBR_CENTRES_FORMATION+NBR_INTERFACES+NBR_APPRENANTS
                  
/* code des compétence en langage des signes et en codage LPC */
#define COMPETENCE_SIGNES     0
#define COMPETENCE_CODAGE     1
                  
/* competences des interfaces en SIGNES et CODAGE*/
int competences_interfaces[NBR_INTERFACES][2]={
    {1,0}, /* compétence en langages des SIGNES mais pas en CODAGE LPC */
    {0,1}, /* pas de compétence en langages des SIGNES mais compétence en CODAGE LPC */
    {0,1},
    {0,1},
    {0,1},
    {0,1},
    {1,0},
    {1,0},
    {0,1},
    {1,0},
    {0,1},
    {1,0},
    {0,1},
    {0,1},
    {1,0},
    {1,0},
    {1,0},
    {0,1},
    {0,1},
    {0,1},
    {0,1},
    {1,0},
    {1,0},
    {0,1}
};
                  
/* spécialités des interfaces */
#define SPECIALITE_SANS       -1 /* Enseigné dans le centre le plus proche */
#define SPECIALITE_MENUISERIE 0
#define SPECIALITE_ELECTRICITE 1
#define SPECIALITE_MECANIQUE 2
#define SPECIALITE_INFORMATIQUE 3
#define SPECIALITE_CUISINE 4
                  
/* specialite des interfaces */
int specialite_interfaces[NBR_INTERFACES][NBR_SPECIALITES]={
    {0,0,0,0,0},
    {0,0,1,0,0},
    {1,0,0,0,0},
    {1,0,0,0,0},
    {0,0,0,0,0},
    {0,0,0,0,1},
    {1,0,1,0,1},
    {1,1,0,0,0},
    {0,0,0,0,0},
    {0,0,0,0,0},
    {0,0,0,0,0},
    {0,0,1,0,0},
    {1,0,0,0,0},
    {1,0,1,0,0},
    {1,0,1,0,0},
    {0,1,0,0,0},
    {0,0,0,0,0},
    {0,0,1,1,1},
    {0,0,0,0,0},
    {0,0,0,0,0},
    {0,0,1,0,0},
    {1,0,1,1,0},
    {0,0,0,1,0},
    {0,0,0,0,0}
};
                  
/* coordonnées des centres de formation, des interfaces et des apprenants */
int coord[NBR_NODES][2]={
                  
    /* Les interfaces se rendent du centre SESSAD à l'école de formation */
    {13,79}, /* centre 0 */
                  
    /* Centres de formation */
    {30,42}, /* ecole formation SPECIALITE_MENUISERIE */
    {96,47}, /* ecole formation SPECIALITE_ELECTRICITE */
    {163,185}, /* ecole formation SPECIALITE_MECANIQUE */
    {116,82}, /* ecole formation SPECIALITE_INFORMATIQUE */
    {134,31}, /* ecole formation SPECIALITE_CUISINE */
                  
    /* Apprenants */
    {170,11}, /* apprenant 0 */
    {80,183}, /* apprenant 1 */
    {109,162}, /* apprenant 2 */
    {99,159}, /* apprenant 3 */
    {21,141}, /* apprenant 4 */
    {175,123}, /* apprenant 5 */
    {83,91}, /* apprenant 6 */
    {88,84}, /* apprenant 7 */
    {163,66}, /* apprenant 8 */
    {106,189}, /* apprenant 9 */
    {114,52}, /* apprenant 10 */
    {31,124}, /* apprenant 11 */
    {165,1}, /* apprenant 12 */
    {157,186}, /* apprenant 13 */
    {157,1}, /* apprenant 14 */
    {40,10}, /* apprenant 15 */
    {192,37}, /* apprenant 16 */
    {149,161}, /* apprenant 17 */
    {174,184}, /* apprenant 18 */
    {149,98}, /* apprenant 19 */
    {100,84}, /* apprenant 20 */
    {98,96}, /* apprenant 21 */
    {20,199}, /* apprenant 22 */
    {103,53}, /* apprenant 23 */
    {159,7}, /* apprenant 24 */
    {57,77}, /* apprenant 25 */
    {76,36}, /* apprenant 26 */
    {117,146}, /* apprenant 27 */
    {106,104}, /* apprenant 28 */
    {4,149}, /* apprenant 29 */
    {63,2}, /* apprenant 30 */
    {26,93}, /* apprenant 31 */
    {96,150}, /* apprenant 32 */
    {103,139}, /* apprenant 33 */
    {129,60}, /* apprenant 34 */
    {50,49}, /* apprenant 35 */
    {150,78}, /* apprenant 36 */
    {113,189}, /* apprenant 37 */
    {132,167}, /* apprenant 38 */
    {100,13}, /* apprenant 39 */
    {173,6}, /* apprenant 40 */
    {159,156}, /* apprenant 41 */
    {111,82}, /* apprenant 42 */
    {138,140}, /* apprenant 43 */
    {40,171}, /* apprenant 44 */
    {151,129}, /* apprenant 45 */
    {185,93}, /* apprenant 46 */
    {28,129}, /* apprenant 47 */
    {124,6}, /* apprenant 48 */
    {161,128}, /* apprenant 49 */
    {154,50}, /* apprenant 50 */
    {87,66}, /* apprenant 51 */
    {59,8}, /* apprenant 52 */
    {135,118}, /* apprenant 53 */
    {147,49}, /* apprenant 54 */
    {65,5}, /* apprenant 55 */
    {16,119}, /* apprenant 56 */
    {169,123}, /* apprenant 57 */
    {97,52}, /* apprenant 58 */
    {79,167}, /* apprenant 59 */
    {183,191}, /* apprenant 60 */
    {9,56}, /* apprenant 61 */
    {76,101}, /* apprenant 62 */
    {117,126}, /* apprenant 63 */
    {34,141}, /* apprenant 64 */
    {112,156}, /* apprenant 65 */
    {185,87}, /* apprenant 66 */
    {143,180}, /* apprenant 67 */
    {169,82}, /* apprenant 68 */
    {26,156}, /* apprenant 69 */
    {123,58}, /* apprenant 70 */
    {115,158}, /* apprenant 71 */
    {6,117}, /* apprenant 72 */
    {128,161}, /* apprenant 73 */
    {26,104}, /* apprenant 74 */
    {50,171}, /* apprenant 75 */
    {28,191}, /* apprenant 76 */
    {174,60}, /* apprenant 77 */
    {7,122}, /* apprenant 78 */
    {149,67}/* apprenant 79 */
};
                  
#define NBR_FORMATION          80
                  
#define LUNDI                  1
#define MARDI                  2
#define MERCREDI               3
#define JEUDI                  4
#define VENDREDI               5
#define SAMEDI                 6
                  
/* formation : id formation, specialite ou centre de formation, competence, horaire debut formation, horaire fin formation */
int formation[NBR_FORMATION][6]={
   {0,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,JEUDI,10,12},
   {1,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,MARDI,16,18},
   {2,SPECIALITE_ELECTRICITE,COMPETENCE_CODAGE,JEUDI,9,11},
   {3,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,JEUDI,16,18},
   {4,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,LUNDI,14,19},
   {5,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,VENDREDI,13,15},
   {6,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,MERCREDI,15,19},
   {7,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,JEUDI,14,17},
   {8,SPECIALITE_ELECTRICITE,COMPETENCE_CODAGE,VENDREDI,9,11},
   {9,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,SAMEDI,9,12},
   {10,SPECIALITE_CUISINE,COMPETENCE_SIGNES,MARDI,13,19},
   {11,SPECIALITE_INFORMATIQUE,COMPETENCE_SIGNES,SAMEDI,8,11},
   {12,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,MERCREDI,9,12},
   {13,SPECIALITE_CUISINE,COMPETENCE_CODAGE,MARDI,15,17},
   {14,SPECIALITE_ELECTRICITE,COMPETENCE_CODAGE,MERCREDI,9,12},
   {15,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,LUNDI,16,18},
   {16,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,VENDREDI,16,19},
   {17,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,SAMEDI,13,16},
   {18,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,SAMEDI,9,11},
   {19,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,SAMEDI,13,19},
   {20,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,MARDI,8,10},
   {21,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,LUNDI,16,18},
   {22,SPECIALITE_CUISINE,COMPETENCE_CODAGE,VENDREDI,15,18},
   {23,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,MERCREDI,16,18},
   {24,SPECIALITE_MENUISERIE,COMPETENCE_CODAGE,JEUDI,14,16},
   {25,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,VENDREDI,14,17},
   {26,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,MERCREDI,15,19},
   {27,SPECIALITE_CUISINE,COMPETENCE_CODAGE,LUNDI,14,17},
   {28,SPECIALITE_ELECTRICITE,COMPETENCE_CODAGE,MERCREDI,8,12},
   {29,SPECIALITE_CUISINE,COMPETENCE_SIGNES,SAMEDI,13,16},
   {30,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,MERCREDI,13,16},
   {31,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,MERCREDI,8,10},
   {32,SPECIALITE_CUISINE,COMPETENCE_SIGNES,SAMEDI,14,18},
   {33,SPECIALITE_INFORMATIQUE,COMPETENCE_SIGNES,MERCREDI,13,17},
   {34,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,SAMEDI,14,16},
   {35,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,VENDREDI,15,17},
   {36,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,SAMEDI,15,17},
   {37,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,MARDI,8,10},
   {38,SPECIALITE_CUISINE,COMPETENCE_SIGNES,SAMEDI,10,12},
   {39,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,MARDI,14,17},
   {40,SPECIALITE_ELECTRICITE,COMPETENCE_CODAGE,LUNDI,14,16},
   {41,SPECIALITE_INFORMATIQUE,COMPETENCE_SIGNES,VENDREDI,9,12},
   {42,SPECIALITE_MENUISERIE,COMPETENCE_CODAGE,JEUDI,13,18},
   {43,SPECIALITE_CUISINE,COMPETENCE_SIGNES,MARDI,10,12},
   {44,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,MARDI,9,12},
   {45,SPECIALITE_CUISINE,COMPETENCE_CODAGE,VENDREDI,16,18},
   {46,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,LUNDI,15,17},
   {47,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,VENDREDI,8,11},
   {48,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,SAMEDI,15,18},
   {49,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,VENDREDI,9,11},
   {50,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,MARDI,9,11},
   {51,SPECIALITE_MENUISERIE,COMPETENCE_CODAGE,SAMEDI,14,17},
   {52,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,SAMEDI,10,12},
   {53,SPECIALITE_ELECTRICITE,COMPETENCE_CODAGE,MARDI,8,10},
   {54,SPECIALITE_CUISINE,COMPETENCE_CODAGE,LUNDI,15,19},
   {55,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,VENDREDI,14,16},
   {56,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,SAMEDI,9,12},
   {57,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,MARDI,14,16},
   {58,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,JEUDI,14,18},
   {59,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,VENDREDI,14,17},
   {60,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,SAMEDI,9,11},
   {61,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,SAMEDI,16,18},
   {62,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,MARDI,16,19},
   {63,SPECIALITE_ELECTRICITE,COMPETENCE_CODAGE,LUNDI,10,12},
   {64,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,JEUDI,13,17},
   {65,SPECIALITE_INFORMATIQUE,COMPETENCE_CODAGE,MARDI,14,16},
   {66,SPECIALITE_INFORMATIQUE,COMPETENCE_SIGNES,VENDREDI,16,18},
   {67,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,SAMEDI,14,18},
   {68,SPECIALITE_MENUISERIE,COMPETENCE_SIGNES,JEUDI,16,18},
   {69,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,MARDI,9,11},
   {70,SPECIALITE_INFORMATIQUE,COMPETENCE_SIGNES,SAMEDI,9,12},
   {71,SPECIALITE_MENUISERIE,COMPETENCE_CODAGE,LUNDI,15,19},
   {72,SPECIALITE_CUISINE,COMPETENCE_SIGNES,SAMEDI,10,12},
   {73,SPECIALITE_MECANIQUE,COMPETENCE_SIGNES,MARDI,14,16},
   {74,SPECIALITE_MENUISERIE,COMPETENCE_CODAGE,LUNDI,13,16},
   {75,SPECIALITE_CUISINE,COMPETENCE_SIGNES,MERCREDI,15,18},
   {76,SPECIALITE_CUISINE,COMPETENCE_CODAGE,SAMEDI,8,11},
   {77,SPECIALITE_ELECTRICITE,COMPETENCE_SIGNES,LUNDI,9,11},
   {78,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,MARDI,9,11},
   {79,SPECIALITE_MECANIQUE,COMPETENCE_CODAGE,MARDI,14,16}
};
                  

void writeCSVfiles() {     FILE *employees_data;
     FILE *coords_data;
     FILE *missions_data;
          employees_data = fopen("./csv/employees_data.csv", "w+");
     coords_data = fopen("./csv/coords_data.csv", "w+");
     missions_data = fopen("./csv/missions_data.csv", "w+");
      fprintf(employees_data, "Signes, LPC, Menuiserie, Electricité, Mécanique, Informatique, Cuisine\n");
     for (int i = 0;
 i < NBR_INTERFACES;
 i++) {         fprintf(employees_data, "%d, %d, %d, %d, %d, %d, %d\n", competences_interfaces[i][0], competences_interfaces[i][1],              specialite_interfaces[i][0], specialite_interfaces[i][1], specialite_interfaces[i][2], specialite_interfaces[i][3]             , specialite_interfaces[i][4]);
     }      fprintf(coords_data, "Centre SESSAD, %d, %d\n", coord[0][0], coord[0][1]);
     fprintf(coords_data, "Centre Formation Menuiserie, %d, %d\n", coord[1][0], coord[1][1]);
     fprintf(coords_data, "Centre Formation Electricité, %d, %d\n", coord[2][0], coord[2][1]);
     fprintf(coords_data, "Centre Formation Mécanique, %d, %d\n", coord[3][0], coord[3][1]);
     fprintf(coords_data, "Centre Formation Informatique, %d, %d\n", coord[4][0], coord[4][1]);
     fprintf(coords_data, "Centre Formation Cuisine, %d, %d\n", coord[5][0], coord[5][1]);
      fprintf(missions_data, "ID, Specialité (Menuiserie-Cuisine = 0-4), Compétence (Codage/LPC = 0/1), Jour (Lun-Sam = 1-6), Horaire Début (h), Horaire Fin (h), Coordonnées X, Coordonnées Y\n");
     for (int i = 0;
 i < NBR_FORMATION;
 i++) {         fprintf(missions_data, "%d, %d, %d, %d, %d, %d, %d, %d\n", formation[i][0], formation[i][1], formation[i][2], formation[i][3],             formation[i][4], formation[i][5], coord[i + 6][0], coord[i + 6][1]);
     } }                  

int main() {
                  
    printf("NBR_INTERFACES=%d\n",NBR_INTERFACES) ;
    printf("NBR_APPRENANTS=%d\n",NBR_APPRENANTS) ;
    printf("NBR_FORMATIONS=%d\n",NBR_FORMATIONS) ;
    printf("NBR_NODES=%d\n",NBR_NODES) ;
                  
    writeCSVfiles();
                  
    return 0 ;
}
                  
