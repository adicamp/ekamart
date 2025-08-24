// Sidebar dynamic builder
(function() {
  const currentPath = (window.__SIDEBAR_CURRENT_PATH__ || window.location.pathname).replace(/\/$/, '') || '/';
  const rootEl = document.getElementById('sidebar-menu-root');
  if (!rootEl) return;
  const openStateKey = 'sidebar.open.keys.v1';
  let persistedOpen = [];
  try { persistedOpen = JSON.parse(localStorage.getItem(openStateKey) || '[]'); } catch(_) { persistedOpen = []; }

  function iconSvg(name, active) {
    // Allow different base size for specific icons
    const isHome = name === 'home';
    const base = 'shrink-0 ' + (isHome ? 'w-5 h-5' : 'w-4 h-4') + ' transition duration-75';
    const passiveColor = 'text-gray-400 dark:text-gray-500';
    const activeColor = 'text-blue-600 dark:text-blue-400';
    // Home icon stays blue (brand) regardless of active state
    const color = isHome ? activeColor : (active ? activeColor : passiveColor);
    switch (name) {
      case 'folder': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 6a2 2 0 0 1 2-2h3l2 2h7v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6Z"/></svg>`;
      case 'inventory': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="14" height="10" rx="2"/><path d="M3 9h14"/></svg>`;
      case 'inventory_dc': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="6" width="12" height="8" rx="2"/><path d="M6 9h4"/><path d="M6 11h6"/></svg>`;
      case 'inventory_toko': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="5" width="12" height="9" rx="2"/><path d="M8 9h4"/></svg>`;
      case 'calendar': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="4" width="14" height="12" rx="2"/><path d="M3 8h14"/></svg>`;
      case 'jwk_toko': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="5" width="12" height="10" rx="2"/><path d="M4 9h12"/></svg>`;
      case 'supplier_reguler': return `<svg class="${base} ${color}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8.5" cy="16.5" r="1.5"/><circle cx="16.5" cy="16.5" r="1.5"/><path d="M3 7h11v9H3zM14 11h3.8l2.2 2v3H14z"/></svg>`;
      case 'supplier_bkl': return `<svg class="${base} ${color}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8.5" cy="16.5" r="1.5"/><circle cx="16.5" cy="16.5" r="1.5"/><path d="M3 7h11v9H3zM14 11h4l2 2v3H14z"/><path d="M6 10h5"/></svg>`;
      case 'store_registration': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 7 4 3h12l1 4"/><path d="M4 7v8a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V7"/></svg>`;
      case 'product_per_supplier': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="4" y="4" width="12" height="12" rx="2"/><path d="M7 8h6M7 12h4"/></svg>`;
      case 'users': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8" cy="8" r="3"/><path d="M2.5 15c.8-2 2.7-3 5.5-3s4.7 1 5.5 3"/></svg>`;
      case 'rak': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 6h12M4 10h12M4 14h12"/></svg>`;
      case 'shelving': return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 5v10M14 5v10M4 8h12M4 12h12"/></svg>`;
  case 'home': return `<svg class="${base} ${color}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 11.5 12 4l9 7.5"/><path d="M5 10v9h14v-9"/><path d="M10 18v-5h4v5"/></svg>`;
      default: return `<svg class="${base} ${color}" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="10" cy="10" r="6"/></svg>`;
    }
  }

  const levelPadding = ['pl-2','pl-6','pl-9','pl-12'];

  function buildItems(items, level = 0) {
    return items.map((item, idx) => {
      const isItem = item.type === 'item';
  const rawUrl = item.url || '';
  const normalizedUrl = rawUrl === '/' ? '/' : rawUrl.replace(/\/$/, '');
  const active = isItem && normalizedUrl === currentPath;
      const padding = levelPadding[Math.min(level, levelPadding.length-1)];
      if (isItem) {
      const isDashboardRoot = level === 0 && item.key === 'dashboard';
      const leading = (level === 0) || (level >= 1 && level <= 2) ? iconSvg(item.icon || 'folder', active || isDashboardRoot) : '<span class="w-4 h-4"></span>';
      if (isDashboardRoot) {
        return `<li role="treeitem"><a href="${item.url}" class="root-group-btn flex items-center w-full gap-3 ps-2 pe-2 py-2 rounded-lg text-sm font-semibold tracking-wide text-gray-800 dark:text-gray-100 transition-colors duration-200 bg-white/90 dark:bg-gray-800/70 hover:bg-blue-50/50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-600 shadow-sm ${active? 'sidebar-item-active':''}" data-menu-key="${item.key}">${leading}<span class="flex-1 text-left">${item.label}</span></a></li>`;
        }
        return `<li role="treeitem"><a href="${item.url}" class="flex items-center w-full gap-2 p-2 rounded-md ${padding} text-xs text-gray-800 dark:text-gray-100 transition-colors duration-150 group hover:bg-gray-100 dark:hover:bg-gray-700 ${active? 'sidebar-item-active':''}" data-menu-key="${item.key}">${leading}<span class="truncate">${item.label}</span></a></li>`;
      }
      // group / submenu
      const nodeId = `menu-${item.key}-${idx}`;
      const childHtml = buildItems(item.children || [], level + 1);
      const childActive = /sidebar-item-active/.test(childHtml); // descendant truly active
      const expanded = childActive || persistedOpen.includes(item.key);
      if (level === 0) {
        const accentState = childActive ? 'scale-100 opacity-100' : 'scale-90 opacity-60';
        return `<li role="treeitem" aria-expanded="${expanded}" class="mt-2 first:mt-0"><button type="button" aria-controls="${nodeId}" aria-expanded="${expanded}" class="menu-toggle root-group-btn flex items-center w-full gap-3 ps-2 pe-2 py-2 rounded-lg text-sm font-semibold tracking-wide text-gray-800 dark:text-gray-100 transition-colors duration-200 bg-white/90 dark:bg-gray-800/70 hover:bg-blue-50/50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-600 shadow-sm" data-menu-key="${item.key}"><span class="root-accent accent-blue ${accentState}"></span><span class="flex-1 text-left">${item.label}</span><svg class="chevron w-3.5 h-3.5 ms-auto text-gray-500 dark:text-gray-400" fill="none" viewBox="0 0 10 6" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="m1 1 4 4 4-4"/></svg></button><div id="${nodeId}" class="menu-collapsible ${expanded? '' : 'h-0'}"><ul class="py-1 space-y-1 pt-1">${childHtml}</ul></div></li>`;
      }
      const showIcon = level >= 1 && level <= 2;
      const leading = showIcon ? iconSvg(item.icon || 'folder', childActive) : '<span class="w-4 h-4"></span>';
      return `<li role="treeitem" aria-expanded="${expanded}"><button type="button" aria-controls="${nodeId}" aria-expanded="${expanded}" class="menu-toggle flex items-center w-full gap-2 p-2 rounded-md ${padding} text-sm text-gray-900 dark:text-gray-100 transition-colors duration-150 hover:bg-gray-100 dark:hover:bg-gray-700" data-menu-key="${item.key}">${leading}<span class="flex-1 text-left truncate">${item.label}</span><svg class="chevron w-3 h-3 ms-auto" fill="none" viewBox="0 0 10 6" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="m1 1 4 4 4-4"/></svg></button><div id="${nodeId}" class="menu-collapsible ${expanded? '' : 'h-0'}"><ul class="py-1 space-y-1">${childHtml}</ul></div></li>`;
    }).join('');
  }

  function attachToggleHandlers(container) {
    container.querySelectorAll('.menu-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const key = btn.getAttribute('data-menu-key');
        const panel = document.getElementById(btn.getAttribute('aria-controls'));
        if (!panel) return;
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        if (expanded) {
          panel.style.height = panel.scrollHeight + 'px';
          requestAnimationFrame(() => { panel.style.height = '0px'; });
          btn.setAttribute('aria-expanded', 'false');
          btn.parentElement.setAttribute('aria-expanded','false');
          persistedOpen = persistedOpen.filter(k => k !== key);
        } else {
          panel.style.height = panel.scrollHeight + 'px';
          btn.setAttribute('aria-expanded', 'true');
          btn.parentElement.setAttribute('aria-expanded','true');
          if (!persistedOpen.includes(key)) persistedOpen.push(key);
        }
        localStorage.setItem(openStateKey, JSON.stringify(persistedOpen));
        panel.addEventListener('transitionend', () => {
          if (btn.getAttribute('aria-expanded') === 'true') panel.style.height = 'auto';
        }, { once: true });
      });
    });
  }

  function showSkeleton() {
    rootEl.innerHTML = '<li><div class="skeleton-block"></div></li><li><div class="skeleton-block" style="width:85%"></div></li><li><div class="skeleton-block" style="width:70%"></div></li>';
  }

  showSkeleton();
  fetch(window.__SIDEBAR_MENU_URL__ || '/api/menu/')
    .then(r => r.json())
    .then(data => {
      const html = buildItems(data.menu || []);
      rootEl.innerHTML = html;
      attachToggleHandlers(rootEl);
      // Enforce only one active item based on currentPath
      (function enforceSingleActive(){
        const anchors = rootEl.querySelectorAll('a[data-menu-key]');
        let matchedOnce = false;
        anchors.forEach(a => {
          const href = a.getAttribute('href') || '';
          const norm = href === '/' ? '/' : href.replace(/\/$/, '');
          if (!matchedOnce && norm === currentPath) {
            a.classList.add('sidebar-item-active');
            matchedOnce = true;
          } else if (norm !== currentPath) {
            a.classList.remove('sidebar-item-active');
          }
        });
      })();
      // Collapse groups that were previously expanded but now have no active child
      (function collapseNonActiveGroups(){
        const openKeys = new Set(persistedOpen);
        rootEl.querySelectorAll('.menu-toggle[aria-expanded="true"]').forEach(btn => {
          const key = btn.getAttribute('data-menu-key');
          const panel = document.getElementById(btn.getAttribute('aria-controls'));
          if (!panel) return;
          const hasActive = panel.querySelector('.sidebar-item-active');
          if (!hasActive) {
            btn.setAttribute('aria-expanded','false');
            const li = btn.parentElement;
            if (li) li.setAttribute('aria-expanded','false');
            panel.classList.add('h-0');
            panel.style.height = '0px';
            if (openKeys.has(key)) openKeys.delete(key);
          }
        });
        persistedOpen = Array.from(openKeys);
        localStorage.setItem(openStateKey, JSON.stringify(persistedOpen));
      })();
    })
    .catch(err => {
      rootEl.innerHTML = '<li class="text-red-500 text-xs px-3">Gagal memuat menu</li>';
      console.error('Menu load error', err);
    });
})();
