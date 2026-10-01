/* The Two Trials of Jeanne d'Arc — a documentary apparatus. Vanilla JS, hash routes. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { jeanne: "Jeanne and her party", court: "The judges of Rouen", england: "England and Burgundy", france: "Charles VII's France", reception: "Rehabilitation and memory" };
const LANGS = { la: "Latin", fr: "Middle French", de: "German", en: "English" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("jeanne_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">1429–1456 · Jeanne d'Arc · Charles VII · Pierre Cauchon</span>
      <h1>Two trials, one verdict undone</h1>
      <p class="lede">In the spring of 1429 a girl from Domrémy came to the court of the uncrowned Charles VII at Chinon and said that God had sent her to raise the siege of Orléans and take him to be crowned at Reims. Within five months she had done both. A year later the Burgundians took her at Compiègne and sold her to the English, who had her tried at Rouen for heresy by a court of churchmen under the bishop of Beauvais, Pierre Cauchon. She abjured, took back her abjuration, and was burned on 30 May 1431. Twenty-five years later, at the request of her family and with the king's consent, a papal commission declared the first trial null.</p>
      <p class="readable">This apparatus follows the two trials and the years between through their documents, in public-domain editions with the original beside an English translation: the record of the interrogations, the university's verdict, the abjuration and the sentence, Jeanne's own letters, the Orléans journal, the Burgundian chronicler, Christine de Pizan's poem of 1429, and the witnesses of 1450–1456.</p>
    </div>
  </div>

  <h2>What the apparatus carries</h2>
  ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : `<p class="fine">The first modules are in preparation; the Texts page lists them with their sources.</p>`}

  <h2>The questions it asks</h2>
  <div class="grid g2">
    <div class="panel"><h3>Why a trial for heresy?</h3>
      <p>A prisoner of war could be ransomed. A heretic could not, and a heretic's victories could be called the devil's work: the coronation at Reims would be the gift of a witch. The English paid for the prisoner and the Church supplied the court.</p></div>
    <div class="panel"><h3>What did the abjuration change?</h3>
      <p>On 24 May 1431, in the cemetery of Saint-Ouen, with the executioner's cart waiting, Jeanne put her mark to an abjuration and was sentenced to prison for life. Four days later she was found again in men's clothes, and declared relapsed. The abjuration that saved her life made her death, a week later, lawful.</p></div>
    <div class="panel"><h3>Who undid the verdict, and why?</h3>
      <p>The king she had crowned did nothing for her in 1431. In 1450, with Rouen retaken, he had an inquiry opened; in 1455 the pope commissioned a nullity trial at the request of her mother and brothers; on 7 July 1456 the first trial was declared null. It cleared her name, and his crown.</p></div>
    <div class="panel"><h3>Can the story be played?</h3>
      <p>A companion game, <a href="https://en-nom-dieu.netlify.app/"><em>En nom Dieu</em></a>, is in preparation: as Jeanne, from Chinon to Rouen, and as the judge, Pierre Cauchon. An abjuration will not guarantee her life. Its cards will cite the passages carried here.</p></div>
  </div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texts</span><h1>The corpus</h1>
    <p class="lede">Each module can be read in full, the original beside the English. Planned modules name their sources and wait their turn; what will not be carried is listed with the reason.</p>
    ${D.mods.shipped.length ? `<h2>Carried</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>Planned</h2><div class="grid g2">${D.mods.planned.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">planned</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">Not carried</h2><div class="grid g2">${D.mods.missing.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">not carried</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Loading…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const lang = bilingual ? langPref : "en";
  const langs = [...new Set(sec.units.filter(u => u.orig).map(u => u.lang || t.orig_sprache))];
  const origName = langs.length === 1 ? (LANGS[langs[0]] || "Original") : langs.map(l => LANGS[l] || l).join(" or ");
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← All texts</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · cited as ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + English`], ["orig", origName], ["en", "English"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Source and editorial note</span>
      <p><b>Source.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Cite as ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg" title="${esc(t.pg_label || "")} page.line">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}${u.lang && langs.length > 1 ? ` <span class="fine">(${esc(LANGS[u.lang] || u.lang)})</span>` : ""}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="origcol"><div class="orig" lang="${esc(u.lang || t.orig_sprache)}"${t.rtl ? ' dir="rtl"' : ""}>${esc(u.orig)}</div>${u.tr ? `<div class="translit">${esc(u.tr)}</div>` : ""}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("jeanne_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Compare</span><h1>1431 against 1456</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← All comparisons</a></p><p class="fine">Loading…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(t.autor)}</b><br><span class="fine">${esc(t.jahr)} · ${esc(sec.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}</div>
        <div class="text">${esc(u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← All comparisons</a></p>
    <span class="tag">Compare</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Timeline</span><h1>1429–1456</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Plates</span><h1>Orléans, Reims and Rouen in pictures</h1>
    <p class="lede">${esc(D.plates.lede || "")}</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Sources, method, limits</span><h1>How this apparatus is made</h1>
    <div class="readable">
    <p><b>Public domain only.</b> Every text is carried from a printing that is out of copyright, and its source is named on its page. Modern critical editions and translations in copyright are not used; where the only good edition is modern, the module says so.</p>
    <p><b>The page is the authority.</b> The Latin and French come from the editions of the nineteenth and early twentieth centuries, above all Jules Quicherat's <i>Procès de condamnation et de réhabilitation de Jeanne d'Arc</i> (5 vols., Paris 1841–1849) and Pierre Champion's <i>Procès de condamnation</i> (1920–1921). The machine reading of the scan is corrected against the page image, and every correction that goes beyond the obvious is named in the notes. The editor's text is kept with his spelling; his apparatus of variant readings is not carried, except where a variant matters.</p>
    <p><b>Translations.</b> T. Douglas Murray's English of both trials (1902) is used where it is close to the original, checked against it, and named. Where there is no public-domain English, or Murray is too free, the site gives its own working translation, close to the original and dedicated to the public domain (CC0).</p>
    <p><b>Voices and distances.</b> The record of the condemnation was kept by notaries of a court that meant to condemn, and translated into Latin after the event; the witnesses of 1450–1456 spoke twenty-five years later, to a court that meant to rehabilitate. The Orléans journal was written for the city she saved, the Burgundian chronicler for the duke whose men took her. Each module says who wrote, when and for whom.</p>
    <p><b>Dates.</b> The texts' own dates are given as printed (feast days, the Roman calendar) with the modern equivalent. The year began at Easter in the usage of the time; dates are given in the modern reckoning.</p>
    </div>
    <h2>Sources carried</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>
    ${(D.plates.plates || []).length ? `<h2>Plates</h2><p class="fine readable">${esc(D.plates.credit)}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Could not load the apparatus: ${esc(e.message)}</p>`; });
