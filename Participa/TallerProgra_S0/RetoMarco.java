package TallerProgra_S0;

public class RetoMarco {
    public static void main(String[] args) {

        //Calcular avance diario Marco
            //Horas (entre 8 y 10 horas) - No hay porcentajes -> Random entre 8 y 10
            //Ritmo (entre 10 a 15 km/h) - No hay porcentajes -> Random entre 10 y 15 
            //Clima (lluvia fuerte 10% v-25%, lluvia noraml 30% v-25%, buen clima 60%)
            //Mono (se cansa 25% v-10%, se escapa 15% (pierde 2 horas de recorrido))

        int marcoMovement = 0; //Hay que calcularlo
        int marcoTime = (int) ((Math.random() * 20) + 8);
        int marcoRate = (int) ((Math.random() * 50) + 10);
        int marcoClimatePercent = (int) (Math.random() * 100);
        int marcoMonkeyPercent = (int) (Math.random() * 100);


        //Calcular avance diario Madre
            //Avanza 80km/dia
            //o
            //Horas (entre 6 y 9 horas) - No hay porcentajes -> Random entre 6 y 9
            //Ritmo (6 a 9km/h) - No hay porcentajes -> Random entre 6 y 9
            //Clima (buen tiempo 60%, lluvia 30% v-25%, lluvia fuerte 10% v-50%)
        
        int motherMovement = 80; //Hay que calcularlo
        int motherTime = (int) ((Math.random() * 30) + 6);
        int motherRate = (int) ((Math.random() * 30) + 6);
        int motherClimatePercent = (int) (Math.random() * 100);

        
        //Calcular Distancia Marco-Madre
            //Inicial 350km
            //Si es <50km probabilidad 50% Marco se entera de donde esta su madre distancia -25km
        
        int distance = 350;

        marcoMovement = movement(marcoTime, marcoRate, marcoClimatePercent, marcoMonkeyPercent);
        motherMovement = movement(motherTime, motherRate, motherClimatePercent, 0);

    }

    public int movement(int time, int rate, int climate, int monkey){

        int climateLose = 0;
        if(climate <= 30){
            climateLose = 25;
        } else if (climate <= 10){
            climateLose = 25;
        }

        int monkeyLose = 0
        if(monkey == 0){

        }
        else{
            if(monkey<= 25){
                monkeyLose = 10;
            } else if (monkey <= 15){
                time -= 2; 
                monkeyLose = 0;
            }
        }

        int applyLoses = (rate * (climateLose/100)) + (rate * (monkeyLose/100));

        int hourMov = rate - applyLoses;
        int mov = time * hourMov;
        
        return mov;

    }

}
