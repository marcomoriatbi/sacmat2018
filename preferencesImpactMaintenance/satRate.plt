# File name: avgSemplicity.plt
#set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 1200, 800 
#set terminal pngcairo  transparent enhanced font "arial,50" fontscale 1.0 size 3000, 2250 
#set terminal pngcairo transparent enhanced font "arial,50" size 4000, 3000 
set terminal pngcairo transparent enhanced font "arial,34" size 2500, 1885 
set output 'A_SatRate.png'
#set title "Average Role Number and Assignments (incomplete solver)"
set auto x
set auto y
#set xlabel '{/Symbol b}'
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
set bmargin 10 
#plot 'Semplicity.dat' using 2:xtic(1) ti col fs pattern 2 lt -1 , '' u 3 ti col fs pattern 4 lt -1
#plot 'Semplicity.dat' using 2:xtic(1) ti col, '' u 3 ti col
#plot 'Semplicity.dat' using 2:xtic(1) ti col, '' u 3 ti col
#plot 'Semplicity.dat' using 2:xtic(1) ti col fs pattern 2 lt -1, '' u 3 ti col fs pattern 4 lt -1
plot 'SmallComp180_numeExc12.txt' using 3:xtic(1) fs pattern 3 lt -1 title 'SmallComp t=180', 'Domino180_numeExc19.txt' using 3:xtic(1) fs pattern 0 lt -1 title 'Domino t=180', 'University360_numeExc10.txt' using 3:xtic(1) fs pattern 1 lt -1 title 'University t=360'


#'SmallComp180_numeExc12.txt' using 2:xtic(1) fs pattern 4 lt -1 title 'Average number of assignments per role' 

#plot 'w_0.2/RolesOcc_0.2_timeout_10.dat' using 3:xtic(1) fs pattern 2 lt -1 title '{/Symbol b}=0.2','w_0.3/RolesOcc_0.3_timeout_10.dat' using 3:xtic(1) fs pattern 1 lt -1 title '{/Symbol b}=0.3', 'w_0.5/RolesOcc_0.5_timeout_10.dat' using 3:xtic(1) fs pattern 3 lt -1 title '{/Symbol b}=0.5', 'w_0.8/RolesOcc_0.8_timeout_10.dat' using 3:xtic(1) fs pattern 0 lt -1 title '{/Symbol b}=0.8'

