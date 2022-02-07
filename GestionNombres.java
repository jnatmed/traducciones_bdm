import java.util.*;

public class GestionNombres {
    public static void main(String[] args){
        Hashtable<String, String> nombres=new Hashtable<String, String>();
        int opcion = 0;
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("\n");
        do{
            System.out.println("Elegir una opcion:\n");
            System.out.println("1. Añadir nombre:\n");
            System.out.println("2. Eliminar nombre:\n");
            System.out.println("3. Mostrar todos los nombres");
            System.out.println("4. Salir:\n");
            opcion = sc.nextInt();
            switch (opcion) {
                case 1:
                    String nom, dni;
                    System.out.println("Introduce Nombre: ");
                    nom = sc.next();    
                    System.out.println("DNI: ");
                    dni = sc.next();    
                    break;
                case 2:

                    break;
                case 3:

                    break;
                case 4:

                    break;
            
                default:
                    break;
            }
        }while(opcion!=4);
    }
}