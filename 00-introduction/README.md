# Introduktion

- [ ] Installera ett program att skriva, köra och debugga din kod i, s.k. IDE -- Integrated development environment.
    - Spyder (Används av andra kurser)
    - Visual Studio Code (mest populär)
    - IDLE (inkluderas med officiell Pythoninstallation)
    - PyCharm
    - Sublime Text
    - Notepad++ (endast Windows)
    - Vim, Emacs
- [ ] Skriv ditt första program

```python
print("Hello World!")
```

# Övningsfrågor

Se föreläsning 0, "The computer and the operating system".

## RAM

1. Vad är RAM och hur fungerar den? (nämn adresser, "random")
2. Vad är en bit, byte, nibble, word?
3. Hur mycket RAM har din dator? (Kan hittas under inställningar.)
4. En viss dator har 8 GB (gigabyte RAM-minne. Hur många bitar kan den lagra?
5. Vad är det som gör att vi behöver andra sätt att lagra data utöver RAM?

> 1. "Random Access Memory", varje byte har en adress som dator kan använda för
>    att ladda in, ändra eller lagra data. "Random" betyder att datan kan nås i
>    vilken ordning som helst, jämför med andra sätt att lagra data, t.ex.
>    bandstation eller CD-skivor där datan läses av i ordning när läsarenheten
>    fysiskt rör sig från ena sidan till den andra.
> 2. Bit: etta eller nolla. Byte: 8 bitar. Nibble: 4 bitar. Word: En storlek
>    som datorn väljer att hantera data i oftast 8, 16, 32 eller 64. (moderna
>    datorer oftast 64, numbera börjar 32 bitars datorer bli mindre vanliga.)
> 3. Min har 8 GB. De flesta nya datorer har 8-16 GB.
> 4. En byte har 8 bits, en gigabyte har $10^9$ bytes. 8 GB = $6.4 \cdot 10^10$
> 5. RAM är "volitile", dvs. att datan försvinner när RAM-enheten förlorar
>    strömm. Datorn flyttar istället datan som bör förvaras i längre tid till
>    t.ex hårddisk/SSD-minne.


## CPU

1. Vad är en CPU och hur fungerar den? (nämn registers, instructions)
2. Vilken CPU har din dator? (Kan hittas under inställningar.)


> 1. Enhet som kan läsa in information (kan vara en address, tal, etc.) från
>    RAM till sina i "registers", och kan utföra "instructions" (addera,
>    multiplicera, etc.) på dem.
> 2. Apple M1. Andra datorer kan ha Intel Core iX-XXXX, AMD Ryzen X XXXX.



## Operating System (OS)

1. Vad är ett OS?
2. Vilken OS har din dator?
3. Vad är en terminal? Kan du hitta en på din dator? (Hint: powershell på windows)
4. Vad är en fil, directory, path?
5. Vad är en shell? Ta fram din terminal igen och kör `ls`. Vad ser du?
6. Vad är en process? Kör `ps` för att se info om processen under din shell.
7. Öppna "Task manager" eller "Activity Monitor" på din dator. Känner du igen
   någon av processerna? Kan du se hur mycket av systemets resurser de tar upp?

> 1. Ett operativsystem är ett speciellt mjukvaruprogram som hanterar alla annan mjukvara som körs på datorn.
>
> 2. Korrekta svar: Windows (Oftast), annars MacOS, Linux eller ChromeOS
>
> 3. Terminalen är det traditionella sättet att interragera med en dator. Denna är också det mest hardvunärasättet att hantera operativsystemet.
> 
> 4. En fil är en abstrakt lagringsdel som hanteras av ditt os. Mappar är en typ av fil som innehåller en lista med namn där varje namn innehåller en länk till en fil.En Path är som en adress som beskriver vart en fil/mapp befinner sig i mappstrukturen.
>
> 5. En shell är ett speciellt program som låter dig använda OS-funktion. Det gör exempelvis att du kan skapa och ta bort filer & mappar.
>
> 6. En process är en abstraktion som ges av operativsystem för CPU:n och RAM som kör en instans av ett program. 
> 
> 7. Kännde du igen någon process? 
