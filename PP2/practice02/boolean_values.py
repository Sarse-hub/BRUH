// ===== ПИНЫ ДАТЧИКОВ =====
const int trigFront = A0;
const int echoFront = A1;

const int trigLeft  = A2;
const int echoLeft  = A3;

const int trigRight = A4;
const int echoRight = A5;

// ===== ПИНЫ МОТОРОВ (L298N) =====
const int IN1 = 2;
const int IN2 = 3;
const int IN3 = 4;
const int IN4 = 5;
const int ENA = 9;   // скорость левого мотора
const int ENB = 10;  // скорость правого мотора

// ===== НАСТРОЙКИ =====
int motorSpeed = 150;        // скорость 0-255
int wallDistance = 20;       // если меньше 20 см, считаем что стена
int turnDelay90 = 450;       // время поворота 90 градусов, подбирается
int turnDelay180 = 900;      // время разворота, подбирается

void setup() {
  Serial.begin(9600);

  // Датчики
  pinMode(trigFront, OUTPUT);
  pinMode(echoFront, INPUT);

  pinMode(trigLeft, OUTPUT);
  pinMode(echoLeft, INPUT);

  pinMode(trigRight, OUTPUT);
  pinMode(echoRight, INPUT);

  // Моторы
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  stopMotors();
  delay(1000);
}

void loop() {
  long frontDistance = getAverageDistance(trigFront, echoFront);
  delay(30);
  long leftDistance = getAverageDistance(trigLeft, echoLeft);
  delay(30);
  long rightDistance = getAverageDistance(trigRight, echoRight);
  delay(30);

  Serial.print("Front: ");
  Serial.print(frontDistance);
  Serial.print(" cm | Left: ");
  Serial.print(leftDistance);
  Serial.print(" cm | Right: ");
  Serial.print(rightDistance);
  Serial.println(" cm");

  // Правило правой руки
  if (rightDistance > wallDistance) {
    turnRight();
    moveForwardShort();
  }
  else if (frontDistance > wallDistance) {
    moveForward();
  }
  else if (leftDistance > wallDistance) {
    turnLeft();
    moveForwardShort();
  }
  else {
    turnAround();
  }
}

// ===== ФУНКЦИИ ДВИЖЕНИЯ =====

void moveForward() {
  analogWrite(ENA, motorSpeed);
  analogWrite(ENB, motorSpeed);

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void moveBackward() {
  analogWrite(ENA, motorSpeed);
  analogWrite(ENB, motorSpeed);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

void turnRight() {
  analogWrite(ENA, motorSpeed);
  analogWrite(ENB, motorSpeed);

  // левый вперед, правый назад
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  delay(turnDelay90);
  stopMotors();
  delay(200);
}

void turnLeft() {
  analogWrite(ENA, motorSpeed);
  analogWrite(ENB, motorSpeed);

  // левый назад, правый вперед
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  delay(turnDelay90);
  stopMotors();
  delay(200);
}

void turnAround() {
  analogWrite(ENA, motorSpeed);
  analogWrite(ENB, motorSpeed);

  // разворот
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  delay(turnDelay180);
  stopMotors();
  delay(200);
}

void moveForwardShort() {
  moveForward();
  delay(250);
  stopMotors();
  delay(100);
}

// ===== ФУНКЦИИ ДАТЧИКОВ =====

long getDistance(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(3);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000); // таймаут 30 мкс
  long distance = duration * 0.034 / 2;

  if (duration == 0) {
    return 300; // если нет сигнала, считаем что далеко
  }

  return distance;
}

long getAverageDistance(int trigPin, int echoPin) {
  long d1 = getDistance(trigPin, echoPin);
  delay(10);
  long d2 = getDistance(trigPin, echoPin);
  delay(10);
  long d3 = getDistance(trigPin, echoPin);

  return (d1 + d2 + d3) / 3;
}