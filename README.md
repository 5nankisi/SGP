# SGP
 Implement a simulator for a simplified process manager for a fictional operating system (Fake Operating System). The FOS system assumes that only 15 process descriptors can exist (considering both those in use and those free). Through object-oriented modeling, the following structures should be implemented:
    • Queue of free descriptors (desc_livre)
    • Queue of process descriptors ready to use the CPU (espera_cpu)
    • Reference to the descriptor of the process occupying the CPU (usando_cpu)
    • Queue of processes waiting to use the printer (espera_printer) containing the descriptors of processes waiting for the printer
    • Reference to the descriptor of the process occupying the printer (usando_printer)
    • Queue of processes waiting to use the disk (espera_disco) containing the descriptors of processes waiting to use the disk
    • Reference to the descriptor of the process occupying the disk (usando_disco) The program should:
        • Initialize the data structures; • Consider that, initially, all descriptors are free and therefore belong to the desc_livre structure;
        • Graphically display (initially in text mode) the state of each data structure, indicating which processes are in each structure at each moment in time;
        • Simulate machine cycles, where:
            o Time progresses each time the user presses a key;
            o The visualization of the data structures is updated at each time unit;
            o At each time unit, there is a 50% chance that a new process will be created (removing a descriptor from the desc_livre queue and adding it to the espera_cpu queue);
            o At each time unit, the descriptors in use and the data structures are updated;
            o A process can only occupy the CPU for a maximum of 3 consecutive time units. If, at the end of this time, the process is not finished, it must yield the CPU to the first process in the espera_cpu queue and return to the end of the queue;
            o The use of the printer and the disk should last as long as necessary. Therefore, a process will never move from the usando_printer state back to the espera_printer queue, for example;
    • Each process should have one CPU cycle, one disk cycle, another CPU cycle, and one printer cycle;
    • When creating a new process, its descriptor should be initialized with the following data:
        o Process name/number; o CPU usage time in the first CPU cycle (minimum 1 and maximum 10): an integer value chosen randomly;
        o Disk usage time (minimum 1 and maximum 5): an integer value chosen randomly;
        o CPU usage time in the second CPU cycle (minimum 1 and maximum 10): an integer value chosen randomly;
        o Printer usage time (minimum 1 and maximum 5): an integer value chosen randomly.
        
        Important: Process descriptors are never lost. Once a process is finished, its descriptor returns to the free descriptors queue.
