package chapter6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ClassMemberTest {
    @Test
    void testTwoNubersCanBeAdded() {
        int sum = ClassMember.add(3,8);
    }
}