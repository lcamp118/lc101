package org.launchcode.cheesemvc.models;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

public class Cheese {

        @NotNull
        @Size(min=3, max=15)
        private String name;

        @NotNull
        @Size(min=1 , message = "Description must not be empty")
        private String description;

        private CheeseType type;

        private int cheeseId;
        private static int nextId = 1; //(static field is shared with all instances of class)

        public Cheese(String name, String description) {
            this(); //this will call constructor below to initialize id
            this.name = name;
            this.description = description;
        }

        public Cheese(){
            cheeseId = nextId; //set cheeseId to value of static nextId
            nextId++; //increment id and set nextId to new ID # (this creates unique IDs for each object)
        }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getCheeseId() {
        return cheeseId;
    }

    public void setCheeseId(int cheeseId) {
        this.cheeseId = cheeseId;
    }

    public CheeseType getType() {
        return type;
    }

    public void setType(CheeseType type) {
        this.type = type;
    }
}
