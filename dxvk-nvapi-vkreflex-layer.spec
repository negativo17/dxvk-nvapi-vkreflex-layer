%global upstream_name dxvk-nvapi

Name:           %{upstream_name}-vkreflex-layer
Version:        0.9.2
Release:        1%{?dist}
Summary:        NVIDIA Reflex Vulkan layer
License:        MIT
URL:            https://github.com/jp7677/%{upstream_name}
ExclusiveArch:  x86_64 aarch64

Source0:        %{url}/archive/v%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Patch0:         dxvk-nvapi-system-headers.patch

BuildRequires:  meson >= 1.0
BuildRequires:  gcc-c++
BuildRequires:  vkroots-devel >= 0^20250716git51c3213
BuildRequires:  vulkan-headers

Requires:       vulkan-loader

%description
This Vulkan layer intercepts Vulkan calls made by DXVK-NVAPI, enriches them with
extra data, and forwards to a Vulkan driver that supports VK_NV_low_latency2
device extension.

Setting up this layer enables the Vulkan flavor of NVIDIA Reflex.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
cd layer
%meson -Dabsolute_library_path=false
%meson_build

%install
cd layer
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/vulkan/implicit_layer.d/VkLayer_DXVK_NVAPI_reflex.json
%{_libdir}/libdxvk_nvapi_vkreflex_layer.so

%changelog
* Mon Sep 28 2026 Simone Caronni <negativo17@gmail.com> - 0.9.2-1
- Update to 0.9.2.

* Tue Jan 27 2026 Simone Caronni <negativo17@gmail.com> - 0.9.1-2
- Drop glslang BuildRequires, update description.

* Sat Jan 24 2026 Simone Caronni <negativo17@gmail.com> - 0.9.1-1
- First build.
