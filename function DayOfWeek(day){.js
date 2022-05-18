function DayOfWeek(day){
    if(day==monday){
      console.log("Go for Work");
    }
    else if(day==tuesday){
      console.log("Its a working day");
    }
    else if(day==wednesday){
      console.log("wear color dress");
    }
    else if(day==thursday){
      console.log("its an expiry day for the indian markets");
    }
    else if(day==friday){
      console.log("go to the mosque at 12.30 for the namaz");
    }
    else if(day==saturday){
      console.log("its a weekend");
    }
    else if(day==sunday){
      console.log("time for a movie");
    }
    
    else{
      console.log("invalid Statement");
    }
  }
  
  DayOfWeek("monday");