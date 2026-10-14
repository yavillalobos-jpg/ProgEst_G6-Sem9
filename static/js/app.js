const alertArea = document.getElementById("alert-area");
const queueList = document.getElementById("queue-list");
const counter = document.getElementById("counter");
const capacityInput = document.getElementById("capacity");
const itemInput = document.getElementById("item");

const video = document.getElementById("camera");
const canvas = document.getElementById("snapshot");
const btnCamera = document.getElementById("btn-camera");
const btnPhoto = document.getElementById("btn-photo");

const PHOTO_WIDTH = 320; // se reduce la foto para que pese poco
let mediaStream = null;

async function request(url, method = "GET", body = null) {
  const options = { method, headers: { "Content-Type": "application/json" } };
  if (body) options.body = JSON.stringify(body);
  const response = await fetch(url, options);
  return response.json();
}

function showAlert(message, category) {
  alertArea.innerHTML = "";
  if (!message) return;

  const alert = document.createElement("div");
  alert.className = `alert alert-${category} alert-dismissible fade show`;
  alert.setAttribute("role", "alert");
  alert.textContent = message;

  const close = document.createElement("button");
  close.type = "button";
  close.className = "btn-close";
  close.setAttribute("data-bs-dismiss", "alert");
  close.setAttribute("aria-label", "Cerrar");
  alert.appendChild(close);

  alertArea.appendChild(alert);
}

function createBadge(text, style) {
  const badge = document.createElement("span");
  badge.className = `badge text-bg-${style} ms-2`;
  badge.textContent = text;
  return badge;
}

function createItemElement(item, isFront, isBack) {
  const li = document.createElement("li");
  li.className = "list-group-item text-center";
  if (isFront) li.classList.add("list-group-item-primary");

  if (item.type === "photo") {
    const img = document.createElement("img");
    img.src = item.value;
    img.alt = "Foto en la cola";
    img.width = 160;
    img.className = "img-fluid rounded";
    li.appendChild(img);
  } else {
    const text = document.createElement("span");
    text.className = "fs-5";
    text.textContent = item.value;
    li.appendChild(text);
  }

  if (isFront) li.appendChild(createBadge("frente", "primary"));
  if (isBack) li.appendChild(createBadge("final", "secondary"));
  return li;
}

function render({ items, capacity, size }) {
  counter.textContent = `${size} / ${capacity}`;
  queueList.innerHTML = "";

  if (items.length === 0) {
    const empty = document.createElement("li");
    empty.className = "list-group-item text-center text-muted py-4";
    empty.textContent = "La cola está vacía";
    queueList.appendChild(empty);
    return;
  }

  items.forEach((item, index) => {
    const isFront = index === 0;
    const isBack = index === items.length - 1;
    queueList.appendChild(createItemElement(item, isFront, isBack));
  });
}

function update(state) {
  render(state);
  showAlert(state.message, state.category);
}

/* ---------- Cámara ---------- */

async function startCamera() {
  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    video.srcObject = mediaStream;
    btnPhoto.disabled = false;
    btnCamera.textContent = "Apagar cámara";
  } catch (error) {
    showAlert("No se pudo acceder a la cámara. Revisa los permisos del navegador.", "danger");
  }
}

function stopCamera() {
  if (mediaStream) mediaStream.getTracks().forEach((track) => track.stop());
  mediaStream = null;
  video.srcObject = null;
  btnPhoto.disabled = true;
  btnCamera.textContent = "Encender cámara";
}

async function takePhoto() {
  if (!mediaStream || !video.videoWidth) return;

  canvas.width = PHOTO_WIDTH;
  canvas.height = Math.round((PHOTO_WIDTH * video.videoHeight) / video.videoWidth);
  canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);

  const image = canvas.toDataURL("image/jpeg", 0.7);
  update(await request("/api/queue/enqueue-photo", "POST", { image }));
}

btnCamera.addEventListener("click", () => {
  if (mediaStream) stopCamera();
  else startCamera();
});

btnPhoto.addEventListener("click", takePhoto);

/* ---------- Cola ---------- */

document.getElementById("config-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  update(await request("/api/queue/config", "POST", { capacity: capacityInput.value }));
});

document.getElementById("enqueue-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const state = await request("/api/queue/enqueue", "POST", { item: itemInput.value });
  update(state);
  if (state.category === "success") itemInput.value = "";
  itemInput.focus();
});

document.getElementById("btn-dequeue").addEventListener("click", async () => {
  update(await request("/api/queue/dequeue", "POST"));
});

document.getElementById("btn-peek").addEventListener("click", async () => {
  update(await request("/api/queue/peek"));
});

request("/api/queue").then(render);