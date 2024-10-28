const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const message = document.getElementById("message");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const fireworks = [];
let particles = [];

function random(min, max) {
  return Math.random() * (max - min) + min;
}

class Firework {
  constructor() {
    this.x = random(canvas.width * 0.1, canvas.width * 0.9);
    this.y = canvas.height;
    this.targetY = random(canvas.height * 0.1, canvas.height * 0.4);
    this.speed = random(2, 5);
    this.exploded = false;
    this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
  }

  update() {
    if (!this.exploded) {
      this.y -= this.speed;
      if (this.y <= this.targetY) {
        this.exploded = true;
        for (let i = 0; i < 50; i++) {
          particles.push(new Particle(this.x, this.y, this.color));
        }
      }
    }
  }

  draw() {
    if (!this.exploded) {
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
      ctx.fill();
    }
  }
}

class Particle {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.size = random(1, 3);
    this.speedX = random(-5, 5);
    this.speedY = random(-5, 5);
    this.gravity = 0.05;
  }

  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    this.speedY += this.gravity;
    this.size *= 0.96;
  }

  draw() {
    if (this.size > 0.2) {
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }
}

function animate() {
  ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  if (fireworks.length < 5) {
    fireworks.push(new Firework());
  }

  fireworks.forEach((firework, index) => {
    firework.update();
    firework.draw();
    if (firework.exploded && !particles.some((p) => p.size > 0.2)) {
      fireworks.splice(index, 1);
    }
  });

  particles.forEach((particle, index) => {
    particle.update();
    particle.draw();
    if (particle.size <= 0.2) {
      particles.splice(index, 1);
    }
  });

  requestAnimationFrame(animate);
}

canvas.addEventListener("mousemove", () => {
  fireworks.push(new Firework());
  message.style.display = "block";
});

animate();
