package lang;

import java.util.Arrays;
import java.util.List;
import java.util.function.Supplier;

/**
 * This class is to test jdk8 new language features features
 */
public class JDK8 {

    private interface Defaulable {
        // Interfaces now allow default methods, the implementer may or
        // may not implement (override) them.
        default String notRequired() {
            return "Default implementation";
        }
    }

    private static class DefaultableImpl implements Defaulable {
    }

    private static class OverridableImpl implements Defaulable {
        @Override
        public String notRequired() {
            return "Overridden implementation";
        }
    }

    private interface DefaulableFactory {
        // Interfaces now allow static methods
        static Defaulable create( Supplier< Defaulable > supplier ) {
            return supplier.get();
        }
    }

    public static class Car {
        public static Car create( final Supplier< Car > supplier ) {
            return supplier.get();
        }

        public static void collide( final Car car ) {
            System.out.println( "Collided " + car.toString() );
        }

        public void follow( final Car another ) {
            System.out.println( "Following the " + another.toString() );
        }

        public void repair() {
            System.out.println( "Repaired " + this.toString() );
        }
    }

    public static class MazdaCar extends Car {
    }

    private static void tryLambda() {
        Arrays.asList("a", "b", "d").forEach(e -> {
            System.out.print(e);
            System.out.print(e);
        });
    }

    private static void tryDefault() {
        Defaulable defaulable = DefaulableFactory.create( DefaultableImpl::new );
        System.out.println( defaulable.notRequired() );

        defaulable = DefaulableFactory.create( OverridableImpl::new );
        System.out.println( defaulable.notRequired() );
    }

    private static void tryMethodRef() {
        final Car car = Car.create( Car::new );
        final Car mazda = Car.create( MazdaCar::new );
        final List< Car > cars = Arrays.asList( car, mazda );

        cars.forEach( Car::collide );
        cars.forEach( Car::repair );
    }

    public static void main(String[] args) {
        // tryLambda();
        // tryDefault();
        tryMethodRef();
    }
}