package chapter8;

public enum School {
    FUPRE("Federal university of Petrolum Resources School", "Warri"),
    UNILAG("University of Lagos", "Lagos"),
    UNN("University of Nigeria", "Nsukka"),
    FUTA("Federal University of Technology", "Akure"),
    FUTO("Federal university of Owerri", "Owerri"),
    FUTMINNA("Federal university of Minna", "Minna"),
    CU("Convenant University", "Lagos"),
    UNIPORT("University of Porthcourt", "Portharcourt");

    private final String fullName;
    private final String location;

    School(String fullName, String location){
        this.fullName = fullName;
        this.location = location;
        System.out.println("i am create" + fullName);
    }

    public String getFullName() {
        return fullName;
    }

    public String getLocation() {
        return location;
    }
}
